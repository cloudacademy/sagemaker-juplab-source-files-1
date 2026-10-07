# E179 Model Selection Evaluation and Specification

This five-hour performance assessment asks you to specify, evaluate and recommend a security classifier. You will submit three written reports supported by reproducible evidence. You choose the analysis and justify your decisions. The prepared environment, starter notebook and utilities remove setup work; they do not supply your conclusions.

## Scenario and business assumptions

An organisation is evaluating phishing-risk scoring before SOC review. It processes approximately 1.2 million web events daily. A separate feature service supplies the 30 encoded indicators used in this assessment. False negatives can leave phishing undetected; false positives consume analyst time and can disrupt legitimate browsing if blocking is introduced.

The initial proposal targets at least 90% recall and at most 1% false-positive rate, with capacity for 15,000 alerts per day. Estimated production phishing prevalence is 0.1%; assess sensitivity to this assumption. Warm model scoring should complete within 250 ms at P95. Customer event data must remain in the organisation's approved AWS geography. The supplied public data contains extracted indicators, not customer traffic or raw URLs. These volumes, targets and constraints are fictional scenario assumptions, not facts established by the dataset. Challenge infeasible or incomplete requirements with evidence.

The initial deployment is analyst triage. Automated blocking requires a separate decision. You may adopt the perspective of an AI/ML Security Assurance Engineer; this persona is context, not an additional assessment requirement. No LLM, Bedrock integration, container, model endpoint or GPU is required.

## Start and work across sittings

Follow WORKSPACE_SETUP.md. Wait for E179_READY.txt in the SageMaker home folder, run E179/notebooks/00_Workspace_Check.ipynb with the E179 v2 Assessment (CPU) kernel, then open the student starter. Your working folder is E179, separate from the GitHub source checkout.

Save notebooks, reports and evidence in outputs/ before breaks. Stop the assigned instance from the SageMaker console. On return, start the same instance, wait for readiness and rerun imports/model-loading cells. The stored files and custom environment survive Stop/Start; memory and running computations do not. Download an export before platform expiry or final submission.

Connection-based idle stopping checks every ten minutes and may stop the instance after thirty idle minutes. Connected clients, non-idle kernels, open terminals, unavailable activity evidence or E179/KEEP_RUNNING keep it running. Automatic stopping is not a backup. Save before closing your browser; manually stop if you need a predictable pause. Remove KEEP_RUNNING after background work.

Additional packages can be installed using `%pip install package-name` in the assessment kernel. Record versions and preserve the supplied core versions, which are required for loading the trained artifacts. Do not change SageMaker's system environment. Use a facilitator-approved separate kernel for incompatible experiments.

## Task 1 Model specification

Define a defensible deployment specification and justify a provisional candidate selection. Compare the supplied Logistic Regression and XGBoost candidates. Reason about model capacity and bias/variance without performing a separate model-development or complexity-tuning exercise.

Your report must address:

- Intended use, stakeholders, harms, deployment assumptions and acceptance criteria.
- Performance, false-positive/false-negative consequences, latency, throughput, cost, geography, explainability and resilience requirements.
- Candidate strengths, limitations and the evidence still needed; distinguish estimates from measurements.
- Relevant governance obligations and approval responsibilities.
- A provisional model choice and what findings would make you reconsider it.

Deliverable: model specification document with a one-page summary. Use templates/Task1_Model_Specification.md or an equivalent structure.

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

The utilities in labkit.py provide model loading, fixed recipes, metrics, confidence intervals and cross-validation. You may inspect, use, adapt or replace them. Explain your method even when you use provided code. There is no prescribed winner or required set of exact scores.

Deliverable: structured model evaluation report with executive summary, findings, interpretation and evidence references. Include your notebook and supporting tables/figures. Use templates/Task2_Evaluation_Report.md or equivalent.

## Task 3 Vendor assessment and procurement recommendation

Assess SecureWeb C using vendor/CLAIMS.md, vendor/TECHNICAL_APPENDIX.md and the supplied prediction files. This is a fictional conventional classifier represented through a restricted evidence packet. You receive scores and labels but no weights, code or facility for new queries. Its withheld implementation creates the black-box constraint; it is not a language model.

Your report must:

- Audit headline claims and benchmark methodology, including sampling, repeated observations, training overlap, thresholds and uncertainty.
- Compare vendor evidence with your candidate results on matched events; explain any comparison limits.
- Identify missing assurance evidence and assess explainability, operational, governance and software supply-chain risk.
- Apply NIST AI RMF to your findings. The source specification allows NIST and/or EU AI Act framing; this implementation uses NIST as the required path. EU AI Act applicability may be discussed if justified, but is not presumed.
- Document mitigations, owners, residual risk and measurable acceptance or rejection conditions.
- Recommend approve, approve with conditions, or reject/seek an alternative. Reconcile this with your provisional selection and the evidence gathered.

Deliverable: vendor assessment and procurement recommendation, including a residual-risk register. Use templates/Task3_Vendor_Recommendation.md and Residual_Risk_Register.csv or equivalent.

## Suggested allocation and submission

Allow approximately 55 minutes for Task 1, 165 minutes for Task 2 and 80 minutes for Task 3. These include writing and export; they are planning estimates, not enforced time limits. Save checkpoints between sittings.

Complete all three report templates. The starter notebook includes an optional export call to report_export.export_all(), which produces Word reports and submissions/E179_submission.zip. It packages your notebooks, output evidence and provenance. Its simple Markdown conversion does not embed figures: include figures manually in your final reports or cite clearly named attached evidence. Review formatting, completeness and references before submitting through the assessment platform. Generating the ZIP does not submit it.

You are assessed on defensible analysis, reproducibility and judgement, not on choosing a predetermined model. State when evidence is insufficient. Do not describe the supplied historical dataset or simulated stress tests as proof of present-day production safety.
