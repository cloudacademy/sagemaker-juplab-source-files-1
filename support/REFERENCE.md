# Supporting reference — E179

You do not need to configure anything in this folder. The assessment notebook loads its files automatically.

Read the dataset and model sections when designing your protocol or interpreting limitations. The vendor packet is under `vendor/` and report outlines are under `templates/`. These are evidence/reference materials; `../README.md` is the only lab instructions file.

# Data card

## Source and licence

Phishing Websites, Rami Mohammad and Lee McCluskey, UCI Machine Learning Repository, DOI https://doi.org/10.24432/C51W2X. Dataset page: https://archive.ics.uci.edu/dataset/327/phishing+websites. UCI lists 11,055 records, 30 integer features and donation on 25 March 2015. It is licensed CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. Credit the authors and UCI, retain this attribution and identify adaptations when redistributing.

This release downloaded the official archive and adapted it into labelled CSVs, curated splits and explicitly simulated fixtures. It does not visit websites or require Kaggle credentials. The source archive hash and transformations are recorded in data/manifest.json. The full original archive is retained privately with the instructor package for reproducibility.

## Curation and schema

Source Result=-1 is mapped to label=1 (phishing); Result=1 becomes label=0 (legitimate). All 30 feature names retain their original ARFF spelling, including typographical errors. Codes are historical heuristic categories, not modern risk probabilities. Use data/schema.json for exact order, allowed values and label mapping. event_id is a source-row identifier, never a predictor. label, event_id and draw_id must be excluded from model input.

357 rows belonging to feature-identical groups with conflicting labels are quarantined. From the remaining consistent groups, 4,977 repeated rows are collapsed, leaving 5,721 distinct feature vectors. Their first source-row ID is retained. No synthetic padding is used to reach 10,000 rows. This curation reduces ambiguity and duplicate leakage but changes the empirical distribution and removes difficult cases; it can make evaluation optimistic and does not reproduce the original population.

The remaining rows are stratified, seeded (179), into training (3,432), validation (1,144) and final holdout (1,145). There are no repeated feature vectors across these splits. Domains and collection timestamps are not supplied, so domain-level independence, temporal generalisation and prospective label availability cannot be established.

## Files and intended use

| File | Role | Dependency or limitation |
| --- | --- | --- |
| training.csv | Fit artifacts and fixed-recipe cross-validation | 1,773 phishing rows; never final test evidence |
| validation.csv | Choose thresholds and protocol | 591 phishing rows; not final performance evidence |
| holdout.csv | Final evaluation after decisions are recorded | 591 phishing rows; historical curated sample |
| demo_sample.csv | Environment smoke test | 120 training rows; not independent evaluation |
| attack_baseline.csv | Baseline for paired stress test | All 591 phishing holdout rows |
| attack_data.csv | Same events, five indicators replaced with code 1 | Label-preserving feature-space simulation, not demonstrated real web attacks |
| shifted_data.csv | Simulated composition shift | 1,145 draws with replacement from holdout; repeated IDs; draw_id identifies draws |

The stress edits affect having_IP_Address, URL_Length, having_At_Symbol, Prefix_Suffix and SSLfinal_State. An attacker is hypothesised to make these indicators appear more legitimate while preserving phishing intent. Joint feature consistency and practical feasibility are not established. Measure conditional evasion among cases detected at baseline; do not infer FPR from all-positive attack data.

The shift fixture weights SSLfinal_State=1 five times as heavily as other rows. It is not a future production snapshot or independent sample. Compare distributions and labelled performance, while recognising resampling dependence. Feature strata such as SSLfinal_State and web_traffic support operational subgroup analysis. No protected attributes are available; demographic fairness cannot be concluded.

## Deployment limits

Historical features include TLS heuristics, popularity, search indexing and statistical blacklist indicators. Some depend on external information or page content unavailable at initial request time. Their validity, extraction cost and availability at the decision timestamp require investigation. Features derived from later reputation knowledge could create target leakage in a prospective deployment. The supplied dataset cannot settle that question.

The curated phishing fraction is approximately one half. It is not the scenario's estimated 0.1% production prevalence. Precision and alert workload will differ substantially under a different class balance, even if recall and FPR transfer. The source is suitable for a bounded teaching assessment; it is insufficient for present-day deployment certification.

## Feature documentation

data/feature_dictionary.csv gives plain-language meanings and allowed source codes for all 30 inputs. Treat each code as a category; do not infer that the numerical code is a probability or universally monotonic risk scale. Detailed historical extraction rules are available in the official UCI archive’s Phishing Websites Features.docx linked from the dataset page. Those rules describe the source methodology, not current security best practice. The assessment works on supplied indicators and does not require implementing a web feature extractor.


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
