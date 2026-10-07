# Candidate model cards

Both candidate artifacts are supplied pretrained for this assessment: the publisher fitted them on training.csv before packaging. They are educational models trained on the public UCI features, not pre-existing commercial detectors or externally validated security products. Students load and evaluate them; they do not need to train or deploy a model to begin.

| Candidate | Design and inference artifact | Evaluation considerations |
| --- | --- | --- |
| Logistic Regression | OneHotEncoder followed by LogisticRegression; the fitted pipeline is stored in models/logistic.joblib | Additive categorical effects; coefficients available; limited interaction representation |
| XGBoost | 160 trees, depth 4, learning rate 0.07, regularisation 3, CPU histogram training; models/xgboost.ubj | Nonlinear interactions; feature codes treated as ordered splits; investigate sensitivity and generalisation |

The encoder uses an explicit [-1,0,1] category vocabulary for each feature; the source contains only a subset for some features. No scaler or data-derived transformation is hidden. XGBoost consumes the 30 feature columns in the schema order. Models return two-class predict_proba outputs; column 1 is the phishing score. A score need not be well calibrated. Classification requires a stated threshold; 0.5 is only the default.

models/provenance.json records training-data SHA-256, software versions, feature order, recipe and artifact hashes. labkit.load_models() checks core versions and hashes before loading. It refuses an incompatible environment rather than silently changing results. Use only the trusted supplied joblib file: pickle-based deserialisation can execute code. Hashes detect accidental changes but do not authenticate a maliciously replaced release.

The instructor preparation code fits the frozen recipes, exports them, loads them back and checks prediction equality. No fit call is used in normal student loading. Cross-validation is separate: labkit.cross_validate() clones each recipe and refits it inside each training fold, with preprocessing inside the pipeline. This evaluates the procedure without leaking fitted preprocessing across folds. A pre-fitted model scored repeatedly on its own training set would not be valid cross-validation.

No model is declared the assessment winner. Neither has production latency, contemporary recall, resilience, geography enforcement or fairness certification. Local timing excludes feature extraction and network/service latency. Risk decisions must reflect those evidence limits.
