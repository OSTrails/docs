.. _tutorial_create_metric_tests:

How to create a test (service) following the FTR API
===================================================

Benchmark Assessment Algorithms rely on **FAIR Metric Tests**.

Each test evaluates a specific FAIR requirement and returns a result of:

* ``pass``
* ``fail``
* ``indeterminate``

A test has three main components.

**DCAT description**

  A machine-readable metadata record describing the test.

**API definition**

  An OpenAPI specification describing how to call the test service.

**Test implementation**

  The executable service that performs the assessment.

Tests can be written in any programming language provided they:

* accept the **GUID of a digital object** as input
* return a **JSON result object** containing the outcome

.. _creating_metric_test:

Creating a new FAIR Metric Test
-------------------------------

New tests can be registered using **FAIR Wizard**.

1. Open FAIR Wizard and create a **new project**.
2. Select a knowledge model.
3. Enable **Filter by question tags**.
4. Choose **Test** as the artefact type.

Two key fields must be completed.

**Endpoint URL**

  The service endpoint that executes the test.

**Endpoint URL Description**

  The location of the **OpenAPI description** of the test API.

Once the questionnaire has been completed, create and submit the
resulting document.

After processing, the test record is deposited in the
**OSTrails Assessment Component Metadata Records repository** and
indexed by FAIR Data Point.

The test will then appear in the **FAIR Champion Test Registry** and
can be referenced in your Benchmark Configuration Spreadsheet.

Next steps
----------

Once your Benchmark Assessment Algorithm and tests are defined you can:

* integrate additional **FAIR Metric Tests**
* refine scoring conditions and weights
* run assessments across larger collections of digital objects

This enables automated **community FAIR Benchmark assessments** using
the OSTrails FAIR Champion tool.

Continue with the tutorial:

:ref:`tutorial_fair_benchmark_algorithm`
