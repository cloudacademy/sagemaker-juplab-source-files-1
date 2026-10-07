# Start your E179 assessment workspace

These instructions cover the environment, file handling and supplied model loading. They do not prescribe your evaluation method or recommendations. Allow setup to finish before beginning the five assessed hours.

## 1. Open JupyterLab

1. Launch your assigned lab using the platform. Open its **JupyterLab access** link (the `userdataJupyterLabAccess` output). This opens the SageMaker notebook console page in the assigned Region.
2. Find `wgu-lab-notebook-instance`. If **Stopped**, choose **Start**. Wait until **InService**, then select **Open JupyterLab**.
3. The file browser may open inside the GitHub repository. Navigate up to the SageMaker home folder, `/home/ec2-user/SageMaker`. You should see `E179_SETUP_STATUS.txt`, `e179-setup.log` and, when ready, `E179_READY.txt`.
4. Open the status file. If it says **INSTALLING**, wait and reopen it; the log shows progress. If it says **FAILED**, send the facilitator the error/log. Do not try to rebuild the environment or retrain models yourself. **InService does not mean software installation has finished.**
5. When status is **READY**, open the **E179** folder. Use this working folder throughout. The separate GitHub checkout is source material; do not work in it or use Git pull to update your assessment.

## 2. Check the kernel and model loading

1. In `E179/notebooks`, open `00_Workspace_Check.ipynb`.
2. Click the kernel name at the top right, or use **Kernel → Change Kernel**, and select **E179 v2 Assessment (CPU)**. JupyterLab can ask you to select a kernel when you open the notebook; choose the same one.
3. Choose **Kernel → Restart Kernel and Run All Cells**. If prompted, confirm the restart.
4. Expected: a package/version table, two candidates with **30 features**, valid probabilities for the demo rows, and **WORKSPACE CHECK PASSED**. This is a capability check using a small training-derived demo sample, not an independent assessment result. It must not be reported as holdout performance.
5. If the check fails, keep the error and contact the facilitator. Check you selected the assessment kernel. Do not bypass a model hash/version check.

## 3. Begin your work

1. Open `E179/notebooks/00_Student_Starter.ipynb`, using the same assessment kernel. Save a copy with **File → Save Notebook As**, for example `YourID_Assessment.ipynb`, in `E179/notebooks/`.
2. Run the starter's introductory import/loading cells. The models are already fitted. The starter contains analysis placeholders for you to complete.
3. Read `LAB_INSTRUCTIONS.md`, `DATA_CARD.md`, `MODEL_CARDS.md` and the fictional supplier evidence in `vendor/`. The three tasks cover a model specification, structured evaluation, and vendor/procurement recommendation. There is no Bedrock or LLM activity.
4. Use the supplied report outlines in `templates/`, or an equivalent structure. Put reproducible tables, figures, reports and evidence in `E179/outputs/`. Keep supplied datasets/model files unchanged.

The starter already establishes the import path. Its model-loading pattern is:

```python
from labkit import load_models, load, FEATURES
models = load_models()
demo = load("demo_sample")
phishing_scores = models["Logistic"].predict_proba(demo[FEATURES])[:, 1]
```

`load_models()` loads the fitted Logistic Regression pipeline and XGBoost candidate, checking the package versions and artifact hashes first. The positive class is phishing (`1`). Use the supplied 30 feature columns in order. You do not need an endpoint, model registry, training job or API key to use these models. Do not load model artifacts from unapproved sources. Your selected metrics, thresholds, analysis and recommendations remain assessment decisions.

## 4. Packages, save and pause

All baseline software is installed. If you need an additional package, you may use `%pip install package-name` from an assessment notebook cell. Record the added version and restart the kernel if required. Preserve the supplied scientific versions: changing them can break saved-model compatibility. Ask the facilitator for a separate kernel if a package needs conflicting versions. Do not install into SageMaker's system environment.

Save with **Ctrl+S** (or **Cmd+S**) regularly. Before a break, save notebooks and reports, then use the SageMaker console **Stop** action for a predictable pause. Close browser tabs and shut down unused terminals after saving. Automatic idle stopping checks every ten minutes and may stop after thirty idle minutes; a connected client, busy kernel or open terminal can keep the instance running. It cannot save unsaved edits.

For deliberate background work, you can create a plain empty file named `KEEP_RUNNING` directly in `E179/` through the JupyterLab file browser (New Text File, then rename). Delete it when no longer needed. This prevents auto-stop, not platform expiry or a manual Stop. Use it only within the lab's resource policy.

To resume, Start the **same assigned instance**, reopen JupyterLab, wait for READY, select the assessment kernel, and rerun imports/loading cells. Saved files and compatible installed packages persist; variables and running jobs do not. Download your notebooks, reports and evidence before platform expiry and for final submission. Stack deletion/account reset can remove the workspace; a platform pause is not a guaranteed backup.

## Where files belong

| Location | Purpose |
| --- | --- |
| `E179/notebooks/` | Workspace check, supplied starter and your saved assessment notebook |
| `E179/data/` | Supplied fixed datasets and schema |
| `E179/models/` | Supplied fitted models, hashes and provenance |
| `E179/vendor/` | Fictional supplier evidence packet |
| `E179/templates/` | Optional report structures |
| `E179/outputs/` | Your evidence, figures and report exports |
| `e179-env/` outside E179 | Prepared kernel environment; do not move/rename |

Ask for help with readiness, access or file/schema errors. The assessment expects you to decide and justify the analysis; setup assistance does not supply the solution.
