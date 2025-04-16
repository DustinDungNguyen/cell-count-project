# Database Schema Prototype

## Tables

### projects
- **project_id** (Primary Key): Unique identifier for each project.
- **project_name**: Name of the project.
- **description**: Brief description of the project.

### patients
- **patient_id** (Primary Key): Unique identifier for each patient.
- **project_id** (Foreign Key): Links to the projects table.
- **diagnosis**: e.g. melanoma, bladder cancer, etc.
- **gender**: Male/Female.
- **age**: Patient age.
- **other_demographics**: Additional demographic info as needed.

### samples
- **sample_id** (Primary Key): Unique identifier for each sample.
- **patient_id** (Foreign Key): Links to the patients table.
- **sample_type**: e.g. PBMC, tissue.
- **time_from_treatment_start**: Time indicator (e.g., baseline if 0).
- **treatment**: Treatment identifier e.g. 'tr1'.
- **response**: Response indicator: 'y' (responder) or 'n' (non-responder).
- **collection_date**: Date of sample collection.

### cell_counts
- **sample_id** (Foreign Key): Links to the samples table.
- **b_cell**: Count of B cells.
- **cd8_t_cell**: Count of CD8+ T cells.
- **cd4_t_cell**: Count of CD4+ T cells.
- **nk_cell**: Count of NK cells.
- **monocyte**: Count of monocytes.

## Advantages of Capturing This Information in a Database

- **Scalability**: Easily store and manage thousands of samples across multiple projects.
- **Data Integrity and Consistency**: Normalized tables reduce redundancy and ensure data integrity.
- **Efficient Querying and Analytics**: Ability to perform complex joins and aggregations across patients, samples, and cell counts for diverse analyses.
- **Flexibility for Analytics**: Supports a wide range of queries (e.g., responders vs. non-responders, breakdown by demographics) and integration with statistical and machine learning tools.
- **Data Security and Access Control**: Enables roles and permissions for secure data access.
