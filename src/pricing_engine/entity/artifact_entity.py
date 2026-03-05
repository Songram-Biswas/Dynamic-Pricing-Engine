from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    message: str
    validation_report_file_path: str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str
@dataclass(frozen=True)
class ModelTrainerArtifact:
    trained_model_file_path: Path
    r2_score: float    