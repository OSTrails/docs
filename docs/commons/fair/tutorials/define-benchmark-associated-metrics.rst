registering.. _tutorial_create_fair_benchmark:

Defining a FAIR Benchmark with its Associated Metrics
=====================================================

This tutorial explains how to create a **community FAIR Benchmark** and
any additional **Metrics** using the OSTrails FAIR Assessment framework.

You will start from the *OSTrails FAIR Assessment – Conceptual Requirements*
template and work through it to produce a **Benchmark narrative** describing
how your community interprets the FAIR Principles for a specific type of
digital object.

By the end of this tutorial you will have:

* a completed **community FAIR Benchmark narrative**
* a defined set of **FAIR Metrics**
* any required **community-specific specialised Metrics**

For an overview of the process, see :ref:`benchmark_workflow`.

.. _benchmark_prerequisites:

Prerequisites
-------------

Before starting you should:

* Download the
  `OSTrails FAIR Assessment – Conceptual Requirements template
  <https://zenodo.org/records/18488022>`_.
* Be familiar with the **FAIR Principles**.
* Identify the **community or discipline** for which the Benchmark will apply.

.. _benchmark_workflow:

Workflow overview
-----------------

Creating a FAIR Benchmark typically involves the following steps:

1. :ref:`copy_template`
2. :ref:`define_benchmark`
3. :ref:`review_generic_metrics`
4. :ref:`define_specialised_metrics`
5. :ref:`review_benchmark`
6. :ref:`register_benchmark`

Each step is described in the sections below.

.. _copy_template:

Step 1 – Copy the OSTrails template
-----------------------------------

Begin by making a working copy of the **OSTrails FAIR Assessment –
Conceptual Requirements template**.

The template provides a structured format for describing:

* the **scope of the Benchmark**
* the **digital objects being assessed**
* the **Metrics used to evaluate FAIRness**
* the **community standards and practices** that apply

Once the template has been downloaded and renamed, you should
work through your Benchmark narrative document sequentially,
completing each section with information relevant to your community.

Proceed to
:ref:`define_benchmark`.

.. _define_benchmark:

Step 2 – Define the community Benchmark
---------------------------------------

The **Benchmark** section provides the narrative description of how
FAIR is interpreted for your community.

Complete the Benchmark description by specifying:

**Benchmark name**

  A short, descriptive title for the Benchmark.

**Description**

  A concise explanation of the purpose of the Benchmark and the
  community it serves.

**Applicability**

  Define clearly:

  * the **type of digital object** being assessed
    (for example datasets, workflows, software, or metadata records)
  * the **disciplinary scope** of the Benchmark

**Related resources**

  List any standards, repositories, policies, or vocabularies that
  support FAIR practice in your community.

The goal of this section is to describe **what FAIR means in practice
for the community and its digital objects**.

Next, review the Metrics available in your Benchmark narrative as described in
:ref:`review_generic_metrics`.

.. _review_generic_metrics:

Step 3 – Review the generic FAIR Metrics
----------------------------------------

Your Benchmark narrative includes **generic Metrics** aligned with the
FAIR Principles. These are designed to be broadly applicable across many
disciplines.

For each Metric card in your Benchmark narrative:

1. Read the description of the Metric.
2. Decide whether it satisfies your community requirements.
3. Select the appropriate option in your Benchmark narrative:

   * ``This generic Metric is sufficient for our needs``
   * ``This generic Metric is not sufficient for our needs``
   * ``This principle is not applicable to our definition of FAIR``

Generic Metrics commonly address topics such as:

* persistent identifiers
* structured metadata
* links between data and metadata
* indexing for discovery
* open and standardised access protocols

In many cases these generic Metrics can be adopted without modification.

If a generic Metric does not fully capture community practice, define a
specialised Metric as described in
:ref:`define_specialised_metrics`.

.. _define_specialised_metrics:

Step 4 – Define specialised Metrics where required
--------------------------------------------------

Some FAIR principles require **community-specific interpretation**.
Where the generic Metric does not adequately represent community
practice, define a **specialised Metric**.

Specialised Metrics are commonly required for principles such as:

* **I2 – Use of FAIR vocabularies**
* **R1.2 – Provenance**
* **R1.3 – Community standards**

When defining a specialised Metric, include the following elements.

**Metric name**

  A short descriptive title.

**Metric description**

  A clear explanation of what is being evaluated and why it supports
  FAIR.

**Assessment criteria**

  The conditions that must be met for the Metric to pass.

**Related standards or resources**

  References to relevant community standards, vocabularies, or
  policies.

**Examples**

  Where possible, provide:

  * a positive example
  * a negative example
  * an indeterminate example

These examples help both implementers and assessment tools understand
how the Metric should be applied.

Once specialised Metrics have been defined, review the Benchmark as
described in :ref:`review_benchmark`.

.. _review_benchmark:

Step 5 – Review the completed Benchmark
---------------------------------------

After completing all sections of your Benchmark narrative:

* Review the Benchmark with **community experts or stakeholders**.
* Check that **all relevant FAIR principles are addressed**.
* Ensure that any referenced **standards, vocabularies, or
  repositories** are clearly identified.

The completed document now represents the **conceptual FAIR Benchmark**
for your community.

The final step is to register the Benchmark and Metrics as described in
:ref:`register_benchmark`.

.. _register_benchmark:

Step 6 – Register the Benchmark and Metrics
-------------------------------------------

To enable reuse and interoperability, the Benchmark and its Metrics
should be converted from a narrative document into both FTR specification documents and registered in community registries such as
`FAIRsharing <https://fairsharing.org>`_.

Conversion to FTR and registration with FAIRsharing should include:

* the **Benchmark description**
* each **specialised Metric**
* references to any **standards, databases, or vocabularies**

Registering in FAIRsharing these components allows:

* FAIR assessment tools to discover and implement the Metrics
* other communities to reuse or adapt the Benchmark
* FAIR assessment results to be compared across tools

More information on how to create formal FTR specification documents and registering them with FAIRsharing is available in our tutorials on specifying and registering `benchmarks <register-benchmark.html>`_ and `metrics <register-metric.html>`_.

Next steps
----------

Once the conceptual Benchmark has been created, the next stages
typically include:

* implementing **machine-actionable Metric tests**
* defining **assessment workflows**
* applying the Benchmark to **evaluate digital objects**

This converts the conceptual definition into a working
**FAIR assessment framework**.

Continue with the tutorial:

:ref:`tutorial_create_metric_tests`

