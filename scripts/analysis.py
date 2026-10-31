from scripts.analysis_common import *
from scripts.fetch_data import ensure_data

def run(mode='full'):
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    data=ensure_data(ROOT/'dataset')
    records=json.loads((data/'complaints-2021-05-14_08_16.json').read_text(encoding='utf-8'))
    df=pd.DataFrame([r['_source'] for r in records])
    df=df.loc[df.complaint_what_happened.fillna('').str.strip().ne(''),['complaint_what_happened','product']].drop_duplicates('complaint_what_happened')
    # The rare original product names remain identified in the provenance report.
    counts=df['product'].value_counts();rare=counts[counts<10].index.tolist()
    df['routing_target']=df['product'].where(~df['product'].isin(rare),'Other (rare source products)')
    if mode=='quick':
        df=df.groupby('routing_target',group_keys=False).sample(frac=.2,random_state=42)
    train,test=train_test_split(np.arange(len(df)),test_size=.2,stratify=df.routing_target,random_state=42)
    model=Pipeline([('tfidf',TfidfVectorizer(stop_words='english',min_df=2,max_features=25000,ngram_range=(1,2))),
                    ('classifier',LogisticRegression(max_iter=1000,class_weight='balanced',random_state=42))])
    report,summary,_=classifier_report(model,df.complaint_what_happened.iloc[train],df.complaint_what_happened.iloc[test],
        df.routing_target.iloc[train],df.routing_target.iloc[test],
        'Route complaints to their recorded source product/service category.','product',
        'Duplicate narratives removed before a stratified 80/20 holdout. TF-IDF vocabulary/IDF fit on training narratives only.')
    report['rare_source_products_grouped']=rare
    report['interpretation']='These are source product labels, not assumed names assigned to arbitrary NMF component IDs. Topic discovery in the historical notebook is exploratory, not classification ground truth.'
    return finish(report,summary)
