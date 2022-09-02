"""Project pipelines."""
import sys

sys.path.append("src/kedro_test")

from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from pipelines.processing_pipeline import processing_pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    return {
        "pipeline1": pipeline([processing_pipeline()]),
        "__default__": pipeline([processing_pipeline()]),
    }
