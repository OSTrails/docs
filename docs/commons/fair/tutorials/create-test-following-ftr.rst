.. _tutorial_create_metric_tests:

How to Create and Register a Test following the FTR API
=======================================================

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


.. _creating_metric_test:

Creating a new Test Implementation
----------------------------------
Tests can be written in any programming language provided they:

* either:
  * accept the **GUID of a digital object** as input, OR
  * accept an upload of the Metadata record to be tested
* return a **JSON result object** containing the outcome following the FTR specification
* We highly recommend that Tests follow the FTR API, which defines the routes and HTTP protocols for each kind of test behaviour (e.g. discovery or execution)


Creating and Registering a new FAIR Metric Test DCAT Record
-----------------------------------------------------------

Tests used with the OSTrails Benchmark Algorithms **must** be registered (using a DCAT Descriptor) in the OSTrails Test Registry.  This can be done by:

a. Authoring a test DCAT descriptor "manually", and doing a pull-request on the FAIR Metrics repository.  This will result in the automatic addition of a landing page for your test, but it will not automatically notify FAIRsharing.

or

b. Test descriptors can be authored and registered using **FAIR Wizard**.

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
can be referenced, by the Test ID, in your Benchmark Configuration Spreadsheet.

Next steps
----------

The next thing you probably want to do is to add this test to a benchmark.

There is a semi-automated **community FAIR Benchmark assessments** that can be authored and executed by
the OSTrails FAIR Champion tool.

Continue with the tutorial:

:doc:`register-benchmark`
