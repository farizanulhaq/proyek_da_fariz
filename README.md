# proyek_DA_fariz Dashboard Instruction

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_DA_fariz
cd proyek_DA_fariz
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run steamlit app
```
cd dashboard
streamlit run dashboard.py
```