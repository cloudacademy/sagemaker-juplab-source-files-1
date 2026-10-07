# E179 — start here

This is a **five-hour performance assessment**. Your lab software, datasets and trained models are installed automatically. You do not need to provision infrastructure, download data, install baseline packages or train the supplied models.

## Start in two steps

1. Open **[00_Check_Environment.ipynb](00_Check_Environment.ipynb)** and select **Run → Run All Cells**. If prompted for a kernel, choose the ordinary **Python 3 (`conda_python3`)** kernel. When it shows **READY**, continue. If setup is still running, wait a minute and rerun the check; if it fails, contact your facilitator.
2. Open **[01_Assessment.ipynb](01_Assessment.ipynb)**. Select **E179 Assessment (CPU)** as the kernel, then use **File → Save Notebook As** to save your own copy here, for example `My_Assessment.ipynb`. Run its introductory cells. They automatically load both trained candidates; add your own analysis and written reasoning in the task sections.

You are already in the correct working folder. Do not navigate up to SageMaker home or look for a status text file. **README.md is the only lab instructions file.** The check is operational preparation, not evidence of independent model performance.

## What you need

- **The assessment notebook** is your working notebook. It locates and loads supporting assets automatically; do not move the `support` folder.
- **[support/REFERENCE.md](support/REFERENCE.md)** contains dataset definitions, model provenance and limitations. Read the relevant sections when designing your evaluation or interpreting evidence.
- **support/vendor/** contains the fictional supplier's claims, technical appendix and matched prediction files for Task 3. Begin with `CLAIMS.md` and `TECHNICAL_APPENDIX.md`; these are evidence to assess, not additional lab instructions.
- **support/templates/** contains optional structures for the three reports and residual-risk register. Edit these for the supplied export cell, or use an equivalent structure.
- **outputs/** is where you save your own tables, figures, evidence and exported submissions. The starter's export cell packages reports and saved root-level assessment notebooks into `outputs/submission/`; review before submitting through the platform.

The supporting datasets and model files are already supplied. The notebook imports `support/labkit.py` and uses `load_models()` to load Logistic Regression and XGBoost with version/hash checks. There are no endpoints, API keys, Bedrock calls or LLM activities. Preserve supplied data/model files; do not bypass a failed version/hash check or load unapproved replacement artifacts.

## Scenario

An organisation is evaluating phishing-risk scoring before SOC review. It processes approximately 1.2 million web events daily. A separate feature service supplies the 30 encoded indicators used here. Missed phishing can harm users; false positives consume analyst time and may disrupt legitimate browsing if blocking is introduced.

The initial proposal targets at least 90% recall and at most 1% false-positive rate, with capacity for 15,000 alerts per day. Estimated production phishing prevalence is 0.1%; assess sensitivity to that assumption. Warm scoring should complete within 250 ms at P95. Customer event data must remain in the organisation's approved AWS geography. These are fictional scenario assumptions to assess, not guaranteed outcomes. The supplied public data contains extracted indicators, not customer traffic or raw URLs.

Initial deployment is analyst triage. Automated blocking requires a separate decision. You may adopt the perspective of an AI/ML Security Assurance Engineer; it is context, not an extra assessment requirement.

## Save and resume

Save your notebook and reports regularly. Before a break, save all work and Stop the same assigned notebook instance from the SageMaker console. To resume, Start it, reopen JupyterLab, rerun the quick check and select the assessment kernel. Stored files and compatible added packages persist through Stop/Start; variables and running jobs do not.

Automatic idle stopping checks every ten minutes and may stop after thirty idle minutes. Connected clients, non-idle kernels or open terminals keep it running. Save before closing tabs; auto-stop is not a backup. For deliberate background work, create an empty `KEEP_RUNNING` file here and remove it afterwards, within the lab's resource policy. Download your submission and evidence before platform expiry or final submission; stack deletion/account reset can remove the workspace.

You may add compatible packages from your assessment notebook using `%pip install package-name`. Record their versions and preserve the supplied core versions for saved-model compatibility. Ask the facilitator for a separate kernel if an experiment needs conflicting versions. Do not change SageMaker's system environment.

## Task 1 Model specification

Define a defensible deployment specification and justify a provisional candidate selection. Compare the supplied Logistic Regression and XGBoost candidates. Reason about model capacity and bias/variance without performing a separate model-development or complexity-tuning exercise.

Your report must address:

- Intended use, stakeholders, harms, deployment assumptions and acceptance criteria.
- Performance, false-positive/false-negative consequences, latency, throughput, cost, geography, explainability and resilience requirements.
- Candidate strengths, limitations and the evidence still needed; distinguish estimates from measurements.
- Relevant governance obligations and approval responsibilities.
- A provisional model choice and what findings would make you reconsider it.

Deliverable: model specification document with a one-page summary. Use support/templates/Task1_Model_Specification.md or an equivalent structure.

## Task 2 Structured model evaluation

Design and carry out an evaluation using the provided artifacts. The model files are already fitted. Training is not a setup task. Fixed-recipe cross-validation is required by the specification and necessarily fits fresh models inside each fold; this is evaluation of a learning procedure, not an invitation to develop or tune a new model.

Provide evidence of:

- A sound evaluation protocol: training/validation/holdout roles, leakage controls, fixed-recipe cross-validation, recorded thresholds and reproducibility.
- Appropriate security metrics and uncertainty, including confusion counts, precision, recall, F1, FPR/FNR and a suitable ranking metric. Explain their business significance.
- Operational subgroup analysis, supported by sample sizes and limitations on what can be inferred about bias or fairness.
- Global and local explanations using SHAP and/or LIME, with an assessment of their reliability and limits. Both libraries are available.
- A paired robustness test using attack_baseline.csv and attack_data.csv, and distribution-shift analysis using shifted_data.csv.
- Deployment implications: workload at the proposed prevalence, latency evidence and its limits, failure modes and mitigations.

Use training.csv for cross-validation and validation.csv for threshold decisions. Record your protocol and threshold choices before final holdout testing. Do not adjust them in response to holdout results and then describe that result as independent. Further investigation is allowed if you clearly label it exploratory and explain the need for new independent validation.

The utilities in support/labkit.py provide model loading, fixed recipes, metrics, confidence intervals and cross-validation. You may inspect, use, adapt or replace them. Explain your method even when you use provided code. There is no prescribed winner or required set of exact scores.

Deliverable: structured model evaluation report with executive summary, findings, interpretation and evidence references. Include your notebook and supporting tables/figures. Use support/templates/Task2_Evaluation_Report.md or equivalent.

## Task 3 Vendor assessment and procurement recommendation

Assess SecureWeb C using support/vendor/CLAIMS.md, support/vendor/TECHNICAL_APPENDIX.md and the supplied prediction files. This is a fictional conventional classifier represented through a restricted evidence packet. You receive scores and labels but no weights, code or facility for new queries. Its withheld implementation creates the black-box constraint; it is not a language model.

Your report must:

- Audit headline claims and benchmark methodology, including sampling, repeated observations, training overlap, thresholds and uncertainty.
- Compare vendor evidence with your candidate results on matched events; explain any comparison limits.
- Identify missing assurance evidence and assess explainability, operational, governance and software supply-chain risk.
- Apply NIST AI RMF to your findings. The source specification allows NIST and/or EU AI Act framing; this implementation uses NIST as the required path. EU AI Act applicability may be discussed if justified, but is not presumed.
- Document mitigations, owners, residual risk and measurable acceptance or rejection conditions.
- Recommend approve, approve with conditions, or reject/seek an alternative. Reconcile this with your provisional selection and the evidence gathered.

Deliverable: vendor assessment and procurement recommendation, including a residual-risk register. Use support/templates/Task3_Vendor_Recommendation.md and support/templates/Residual_Risk_Register.csv or equivalent.

## Suggested allocation and submission

Allow approximately 55 minutes for Task 1, 165 minutes for Task 2 and 80 minutes for Task 3. These include writing and export; they are planning estimates, not enforced time limits. Save checkpoints between sittings.

Complete all three report templates. The starter notebook includes an optional export call to report_export.export_all(), which produces Word reports and outputs/submission/E179_submission.zip. It packages your notebooks, output evidence and provenance. Its simple Markdown conversion does not embed figures: include figures manually in your final reports or cite clearly named attached evidence. Review formatting, completeness and references before submitting through the assessment platform. Generating the ZIP does not submit it.

You are assessed on defensible analysis, reproducibility and judgement, not on choosing a predetermined model. State when evidence is insufficient. Do not describe the supplied historical dataset or simulated stress tests as proof of present-day production safety.
