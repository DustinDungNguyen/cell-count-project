-- 1. Summarize the number of subjects available for each condition.
-- (Assuming a column 'condition' exists in the patients table.)
SELECT condition, COUNT(DISTINCT patient_id) AS num_subjects
FROM patients
GROUP BY condition;


-- 2. Return all melanoma PBMC samples at baseline from patients who have treatment 'tr1'.
-- Additionally, include samples for bladder cancer as per the extended requirement.
SELECT s.*
FROM samples s
JOIN patients p ON s.patient_id = p.patient_id
WHERE s.sample_type = 'PBMC'
  AND s.time_from_treatment_start = 0
  AND s.treatment = 'tr1'
  AND p.diagnosis IN ('melanoma', 'bladder cancer');


-- 3a. How many samples from each project for the above selection.
SELECT pr.project_name, COUNT(s.sample_id) AS num_samples
FROM samples s
JOIN patients p ON s.patient_id = p.patient_id
JOIN projects pr ON p.project_id = pr.project_id
WHERE s.sample_type = 'PBMC'
  AND s.time_from_treatment_start = 0
  AND s.treatment = 'tr1'
GROUP BY pr.project_name;


-- 3b. How many responders vs. non-responders.
SELECT s.response, COUNT(s.sample_id) AS num_samples
FROM samples s
WHERE s.sample_type = 'PBMC'
  AND s.time_from_treatment_start = 0
  AND s.treatment = 'tr1'
GROUP BY s.response;


-- 3c. How many males and females.
SELECT p.gender, COUNT(DISTINCT p.patient_id) AS num_patients
FROM patients p
JOIN samples s ON s.patient_id = p.patient_id
WHERE s.sample_type = 'PBMC'
  AND s.time_from_treatment_start = 0
  AND s.treatment = 'tr1'
GROUP BY p.gender;
