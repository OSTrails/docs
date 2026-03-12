.. _tutorial_fair_benchmark_algorithm:

Defining and Running a FAIR Benchmark Assessment Algorithm
===========================================================

This tutorial explains how to define and run a **FAIR Benchmark Assessment
Algorithm** using the OSTrails tool **FAIR Champion**.

A Benchmark Assessment Algorithm combines multiple **FAIR Metric Tests**
and scoring rules to assess the FAIRness of a digital object according to
a specific community Benchmark.

In this tutorial you will:

* run an existing Benchmark assessment
* create your own **Benchmark Configuration Spreadsheet**
* register the algorithm with FAIR Champion
* run the algorithm on one or more digital objects

By the end of this tutorial you will have a working **FAIR Benchmark
Assessment Algorithm** that can be executed within FAIR Champion.

.. _benchmark_algorithm_prerequisites:

Prerequisites
-------------

Before starting you should have completed:

* :ref:`tutorial_create_fair_benchmark`
* :ref:`tutorial_create_metric_tests`

And have access to:

* The **FAIR Champion assessment service**.
* Your **Benchmark definition** and associated metrics.

Some steps also require access to:

* `FAIR Champion <https://tools.ostrails.eu/champion/>`_
* `FAIR Wizard <https://ostrails-fair.fair-wizard.com/>`_
* `OSTrails Test Registry <https://tools.ostrails.eu/champion/tests/>`_

.. _benchmark_algorithm_workflow:

Workflow overview
-----------------

Creating and running a Benchmark Assessment Algorithm (BAA) involves the
following steps:

1. :ref:`run_existing_algorithm`
2. :ref:`create_configuration_spreadsheet`
3. :ref:`register_algorithm`
4. :ref:`run_single_assessment`
5. :ref:`run_multiple_assessments`

Each step is described in the sections below.

.. _run_existing_algorithm:

Step 1 – Run an existing Benchmark assessment
---------------------------------------------

Before creating a new algorithm it is helpful to run an existing one to
confirm that the assessment service is working.

1. Open the FAIR Champion assessment interface:

   https://tools.ostrails.eu/champion/assess/algorithms/new

2. Select a **Benchmark Configuration Spreadsheet URI** from the list.

3. Enter the **GUID of the digital object** to be assessed.

4. Click **Run Benchmark Quality Assessment**.

After a few seconds the results will be displayed on screen.

The output typically shows:

* individual test results
* weighted scores
* conclusions
* optional links to guidance for Conditions that were not met

Running an existing algorithm confirms that the FAIR Champion service
is functioning correctly.

You can now proceed to creating your own configuration spreadsheet as
described in :ref:`create_configuration_spreadsheet`.

.. _create_configuration_spreadsheet:

Step 2 – Create a Benchmark Configuration Spreadsheet
-----------------------------------------------------

Benchmark Assessment Algorithms for FAIR Champion are defined
using a **configuration spreadsheet**.

You can begin by copying the **Generic Algorithm spreadsheet** available
from the FAIR Champion assessment interface.

The spreadsheet contains three sections.

**General metadata**

  Describes the algorithm using DCAT properties.

**Test references**

  Lists the FAIR Metric Tests used by the algorithm and assigns weights
  to their outputs.

**Conditions and calculations**

  Defines the scoring logic based on the test results.
  Links to guidance may be included for some or all of the conditions.

General rules for configuration spreadsheets:

* Currently only **Google Sheets** are supported.
* The spreadsheet must be **publicly readable**.
* Headers must be used **exactly as provided in the template**.
* Each section must be separated by **one empty line**.
* The URIs of the tests must resolve to a **DCAT DataService record**
  describing the test.

A list of available tests can be found in the
`OSTrails Test Registry <https://tools.ostrails.eu/champion/tests/>`_.

Calculations reference tests by their **abbreviation**. Expressions use
Ruby-style syntax, for example::

   test_identifier_1 + test_identifier_2 > 3

Each calculation returns either **true** or **false**, which determines
the narrative result associated with that condition.

Once the spreadsheet is complete it must be registered with FAIR
Champion as described in :ref:`register_algorithm`.

.. _register_algorithm:

Step 3 – Register the Benchmark Assessment Algorithm
----------------------------------------------------

After creating your configuration spreadsheet you must register it so
that FAIR Champion can use it.

1. Ensure the spreadsheet is **publicly accessible**.
2. Copy the **URI of the spreadsheet**.
3. Register the spreadsheet with FAIR Champion via the
   'Register a new Benchmark Quality Assessment Algorithm' option
   on the home page.

FAIR Champion will convert the spreadsheet into a registered
**Benchmark Assessment Algorithm**.

You can verify that the registration succeeded by checking the
**FAIR Data Point index**, where the algorithm should appear with
status **Active**.

Once the algorithm is registered it will appear in the list of
available Benchmark algorithms within the FAIR Champion interface.

You can now run the algorithm as described in
:ref:`run_single_assessment`.

.. _run_single_assessment:

Step 4 – Run an assessment using your algorithm
-----------------------------------------------

To run an assessment using your own algorithm:

1. Return to the FAIR Champion assessment interface:

   https://tools.ostrails.eu/champion/assess/algorithms/new

2. Select your **Benchmark Configuration Spreadsheet URI** from the
   algorithm list.

3. Enter the **GUID of a digital object**.

4. Click **Run Benchmark Quality Assessment**.

If the configuration spreadsheet has been correctly defined and
registered, the results will be displayed in the same way as when
running an existing algorithm.

This confirms that your **Benchmark Assessment Algorithm** is working
correctly.

.. _run_multiple_assessments:

Step 5 – Run assessments on multiple objects
--------------------------------------------

To run assessments on multiple digital objects you can use the
**benchmark runner** application.

1. Clone the repository::

https://github.com/cessda/cessda.cmv.benchmark-runner

2. Build the application::

mvn compile

3. Edit the ``guids.txt`` file so that it contains the GUIDs of the
   digital objects to be assessed.

4. Run the application using::

mvn exec:java -Dexec.args=<algorithm-URL>

where ``<algorithm-URL>`` is the URL of your registered Benchmark
algorithm.

The terminal will display progress as each object is assessed.

Results for each GUID are written to the ``results`` directory.
