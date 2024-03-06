import os
from pathlib import Path

project_name = "us_visa"

list_of_files = [
    
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/data_trainer.py",
    f"{project_name}/components/data_evaluation.py",
    f"{project_name}/components/data_pusher.py",
    
    f"{project_name}/configuration/__init__.py",
    
    f"{project_name}/constant/__init__.py",
    
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    
    f"{project_name}/exception/__init__.py",
    
    f"{project_name}/logger/__init__.py",
    
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    
    f"{project_name}/app.py",
    f"{project_name}/requirements.txt",
    f"{project_name}/Dockerfile",
    f"{project_name}/.dockerignore",
    f"{project_name}/demo.py",
    f"{project_name}/setup.py",
    f"{project_name}/config/model.yaml",
    f"{project_name}/config/schema.yaml",
    f"{project_name}/test.py",
    "test1.py"
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != " ":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.isfile(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"File is already present at: {filepath}")