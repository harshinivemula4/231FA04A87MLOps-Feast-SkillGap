from datetime import timedelta

from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32


# Entity
student = Entity(
    name="student_id",
    join_keys=["student_id"],
    description="Unique identifier for each CSE student"
)


# Data Source
student_features_source = FileSource(
    name="student_features_source",
    path="data/student_features.parquet",
    timestamp_field="event_timestamp"
)


# Feature View
student_skill_features = FeatureView(
    name="student_skill_features",
    entities=[student],
    ttl=timedelta(days=365),

    schema=[
        Field(name="Programming", dtype=Float32),
        Field(name="DSA", dtype=Float32),
        Field(name="DBMS", dtype=Float32),
        Field(name="Computer_Networks", dtype=Float32),
        Field(name="Operating_Systems", dtype=Float32),
        Field(name="Web_Development", dtype=Float32),
        Field(name="Data_Analytics", dtype=Float32),
        Field(name="AI_ML", dtype=Float32),
        Field(name="Cloud_Computing", dtype=Float32),
        Field(name="Cybersecurity", dtype=Float32),
        Field(name="Problem_Solving", dtype=Float32),
        Field(name="Aptitude", dtype=Float32),
        Field(name="Communication", dtype=Float32),
        Field(name="Teamwork", dtype=Float32),
        Field(name="Git_GitHub", dtype=Float32),

        Field(name="technical_skill_average", dtype=Float32),
        Field(name="programming_problem_solving", dtype=Float32),
        Field(name="data_ai_average", dtype=Float32),
        Field(name="cloud_security_average", dtype=Float32),
        Field(name="soft_skill_average", dtype=Float32),
        Field(name="overall_skill_average", dtype=Float32),
        Field(name="overall_industry_gap", dtype=Float32),
        Field(name="curriculum_alignment_score", dtype=Float32),
        Field(name="industry_alignment_score", dtype=Float32),
    ],

    source=student_features_source,
)
