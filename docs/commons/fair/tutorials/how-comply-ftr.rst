FAIR Test Results (FTR) Developer Tutorial
==========================================

.. contents::
   :depth: 2
   :local:

.. toctree::
   :maxdepth: 1
   :hidden:

   others-use-my-metrics
   create-metric
   create-benchmark
   create-test-following-ftr
   define-run-scoring-algorithm
   run-existing-test

Overview
--------

The FAIR Test Results (FTR) specification provides a standard way to define, 
execute, and expose FAIR assessments in a machine-readable and interoperable way.

FTR is built around four core entities:

- **Metric**: A measurable FAIR principle or rule
- **Benchmark**: A collection of metrics
- **Test**: An implementation that evaluates a metric
- **Scoring Algorithm**: A method to aggregate test results into a score

For full reference, see:
https://docs.ostrails.eu/en/latest/commons/fair/fair-test-results-vocabulary-ftr.html


Step 1 - Identification of Metrics
----------------------------------

Most FAIR assessment tools already include a set of tests. The first step is to 
analyse those tests and determine whether they correspond to existing FAIR metrics. These metrics can exist or not

The first step 
is to analyse these tests and determine whether they correspond to existing 
metrics defined in the FAIR Sharing framework.

- If a test can be mapped to an existing metric, follow this tutorial :doc:`others-use-my-metrics`

- If no suitable metric exists, you will need to create new ones by following :doc:`create-metric`

This step is essential to ensure interoperability and reuse of existing  community standards whenever possible.

Guidelines:

- Prefer **reusing existing metrics** to ensure interoperability. 
- Only create new metrics when necessary
- Ensure each metric is clearly defined and documented

Resources:

- Reuse metrics :doc:`others-use-my-metrics` 
- Create new metrics :doc:`create-metric`

Step 2 - Grouping Metrics into a Benchmark
------------------------------------------

A **benchmark** is a logical grouping of metrics used to evaluate a resource.


Key considerations:

- Benchmarks should be **coherent and meaningful**
- You can combine:
  - Existing metrics
  - Newly created metrics
- Benchmarks define the **scope of evaluation**

Resource:

- :doc:`create-benchmark`

Step 3 - API Creation
--------------------

FTR requires a standardised API to expose:

- Tests
- Metrics
- Results
- Scores

Think of FTR as a **contract** your API must follow.


Implementation options:

- Adapt an existing API
- Build a new API following FTR specification

Key requirements:

- Consistent data model
- Standardised endpoints
- Machine-readable outputs (e.g., JSON-LD)

Step 4 - Test Creation
---------------------

Each metric must have at least one corresponding **test**.

A test:

- Implements the logic to evaluate a metric (it is code)
- Produces a result in FTR format


Requirements:

- Align test logic with metric definition
- Ensure reproducibility
- Provide clear outputs

Resource:

- :doc:`create-test-following-ftr`

Step 5 - Scoring Algorithm Implementation
----------------------------------------

The **scoring algorithm** aggregates test results into a final score.


Responsibilities:

- Combine multiple test results
- Produce an overall FAIR score
- Ensure transparency and reproducibility

Best practices:

- Document your scoring method
- Keep it interpretable
- Avoid hidden logic

Resource:

- :doc:`define-run-scoring-algorithm`

Step 6 - Deployment
------------------

Once all components are implemented, deploy your FTR-compliant service.


Checklist:

- API is publicly accessible 
- Endpoints follow FTR specification
- Tests execute correctly
- Scores are computed consistently

Validation:

- :doc:`run-existing-test`


Conclusion
----------

By following this tutorial, you will:

- Align your tool with FTR
- Enable interoperability with other FTR-compliant services
- Provide reproducible and transparent FAIR evaluations


