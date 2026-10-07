"""Small, inspectable assessment utilities; no model choice or report conclusions."""
from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, roc_auc_score, average_precision_score
SEED=179
ROOT=Path(__file__).resolve().parent
FEATURES=json.loads((ROOT/'data/schema.json').read_text())['features']
def load(name): return pd.read_csv(ROOT/'data'/f'{name}.csv')
def recipes():
    from xgboost import XGBClassifier
    return {'Logistic':make_pipeline(OneHotEncoder(categories=[[-1,0,1]]*len(FEATURES),handle_unknown='error',sparse_output=False),LogisticRegression(C=1,max_iter=1500,random_state=SEED)),
            'XGBoost':XGBClassifier(n_estimators=160,max_depth=4,learning_rate=.07,subsample=1,colsample_bytree=1,reg_lambda=3,tree_method='hist',device='cpu',n_jobs=2,random_state=SEED,eval_metric='logloss')}
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load_models(model_dir=None):
    import joblib
    from xgboost import XGBClassifier
    import importlib.metadata as md
    p=Path(model_dir or ROOT/'models'); meta=json.loads((p/'provenance.json').read_text())
    for name,version in meta['versions'].items():
        if md.version(name)!=version: raise RuntimeError(f'{name}: expected {version}; select the E179 Assessment (CPU) kernel or restore requirements.lock.txt')
    for name,digest in meta['artifact_sha256'].items():
        if sha(p/name)!=digest: raise ValueError(f'Artifact hash mismatch: {name}')
    # Only load artifacts from this trusted release. A hash alone does not establish trust.
    a=joblib.load(p/'logistic.joblib')
    b=XGBClassifier();b.load_model(p/'xgboost.ubj');b.set_params(n_jobs=2,device='cpu')
    return {'Logistic':a,'XGBoost':b}
def wilson(k,n,z=1.96):
    if not n:return (np.nan,np.nan)
    p=k/n; d=1+z*z/n; h=z*np.sqrt(p*(1-p)/n+z*z/(4*n*n))/d; m=(p+z*z/(2*n))/d
    return m-h,m+h

def metrics(y,p,t=.5):
    y=np.asarray(y);p=np.asarray(p);pred=(p>=t).astype(int)
    tn,fp,fn,tp=confusion_matrix(y,pred,labels=[0,1]).ravel()
    div=lambda a,b:float(a/b) if b else np.nan
    rlo,rhi=wilson(tp,tp+fn); flo,fhi=wilson(fp,fp+tn)
    return dict(n=len(y),tn=int(tn),fp=int(fp),fn=int(fn),tp=int(tp),threshold=float(t),accuracy=accuracy_score(y,pred),precision=div(tp,tp+fp),recall=div(tp,tp+fn),f1=f1_score(y,pred,zero_division=0),fpr=div(fp,fp+tn),fnr=div(fn,fn+tp),roc_auc=roc_auc_score(y,p) if len(set(y))==2 else np.nan,average_precision=average_precision_score(y,p) if len(set(y))==2 else np.nan,recall_low=rlo,recall_high=rhi,fpr_low=flo,fpr_high=fhi)

def cross_validate(training,folds=5):
    """Refit fresh pipelines in each fold. Never score fitted artifacts on their training rows."""
    rows=[]
    for name,recipe in recipes().items():
        cv=StratifiedKFold(folds,shuffle=True,random_state=SEED)
        for fold,(tr,va) in enumerate(cv.split(training[FEATURES],training.label),1):
            model=clone(recipe).fit(training.iloc[tr][FEATURES],training.iloc[tr].label)
            rows.append(dict(model=name,fold=fold,**metrics(training.iloc[va].label,model.predict_proba(training.iloc[va][FEATURES])[:,1])))
    return pd.DataFrame(rows)
