.. _find-test-for-digital-object:

How to find a Test for my digital object
========================================

This tutorial covers how to find a Test using FAIRsharing (Test linked to a Metric), and how to find Tests using FAIR Champion.


FAIRsharing: Finding a Test Linked to a Metric
-----------------------------------------------

This section explains how to navigate to a metric record in FAIRsharing
and locate any tests that implement it. If you have not yet found a
metric of interest, see :doc:`find-metrics-and-benchmarks` first.

Background: how tests relate to metrics
-----------------------------------------

FAIRsharing registers the conceptual components of the FAIR assessment
ecosystem — Principles, Metrics, and Benchmarks. Tests, which are the
concrete implementations of Metrics, are registered separately in FAIR
Champion at `https://tools.ostrails.eu/champion/tests/
<https://tools.ostrails.eu/champion/tests/>`_. However, FAIRsharing
Metric records provide a cross-reference to any tests that implement
them via the Associated Tests field in the record's Additional
Information section.

Associated tests are cross-referenced in two ways:

- At regular intervals, the FAIRsharing team automatically updates
  the Associated Tests field by querying FAIR Champion and other
  registered test sources.
- Metric maintainers may also add test URLs manually at any time.

.. note::

   FAIRsharing stores URLs pointing to tests; it does not store the
   tests themselves. Each URL may point to an individual test or to a
   search URL that retrieves all tests implementing that metric. An
   optional free-text note field is available alongside each URL to
   provide further context.

For full documentation on the Associated Tests field and the related
Positive and Negative Examples fields, see the `FAIRsharing
documentation on metric tests and examples
<https://fairsharing.gitbook.io/fairsharing/additional-information/metric-tests-and-examples#associated-tests>`_.


A note on object types
-----------------------

Metrics in FAIRsharing are tagged with one or more object types that
describe the kind of digital object the metric is designed to assess.
When looking for a test linked to a metric, it is therefore helpful to
have a clear understanding of what type of digital object you are
working with, so that you can identify the most relevant metrics before
looking for their associated tests.

The full controlled vocabulary of object types is available at
`https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/object-types
<https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/object-types>`_.
The vocabulary includes specific types such as dataset, software
application, model, terminology artifact, and protocol or workflow,
among others. Two general-purpose types are also available:

- *object type agnostic* — used for metrics that apply across all
  types of digital object.
- *other object type* — used only when the object type is not covered
  by any other term in the vocabulary and the resource is not agnostic.

.. note::

   The term *object type not found* appears on a small number of older
   deprecated records where the original object type could not be
   determined during curation. This is an administrative term and is
   not relevant when searching for metrics; you can safely ignore it.

Review the full vocabulary before filtering, as the most appropriate
choice may not always be immediately obvious. For example, a metric
relevant to all digital objects should be found using *object type
agnostic* rather than by listing individual types.


Step 1: Open a metric record
-----------------------------

You can arrive at a metric record in either of two ways.


Via FAIRassist
~~~~~~~~~~~~~~

Navigate to the `FAIRassist registry <https://fairassist.org/registry>`_
and use the filters to find a metric relevant to your needs, as
described in :doc:`find-metrics-and-benchmarks`. Click on any metric
in the results to open its full FAIRsharing record.


Via FAIRsharing directly
~~~~~~~~~~~~~~~~~~~~~~~~

Use the FAIRsharing search or advanced search to find a metric, as
described in :doc:`find-metrics-and-benchmarks`. Alternatively, if
you already have the DOI or URL of a specific metric, navigate directly
to that record. For example:

- `FAIR Metric - A version IRI is declared in the ontology metadata
  <https://doi.org/10.25504/FAIRsharing.99c9f7>`_
  (``https://doi.org/10.25504/FAIRsharing.99c9f7``)
- `FAIR Metric - Metadata Contains CESSDA Provenance Information
  <https://doi.org/10.25504/FAIRsharing.4e4752>`_
  (``https://doi.org/10.25504/FAIRsharing.4e4752``)


Step 2: Navigate to the Additional Information section
-------------------------------------------------------

Once you have a metric record open, scroll down past the General
Information section. FAIRsharing record pages are organised into
tabbed or sectioned areas; look for the Additional Information
section or tab. Within it, you will find the following subsections
specific to metric records:

- Associated Tests
- Positive Examples
- Negative Examples

.. note::

   The Associated Tests, Positive Examples, and Negative Examples
   subsections appear only on records within the FAIRassist registry
   (i.e. Metric records). They are not present on standard database,
   policy, or other FAIRsharing record types.


Step 3: View the Associated Tests
-----------------------------------

The Associated Tests subsection lists one or more URLs, each linking
to a test or set of tests that implement the metric. Each entry may
also include a free-text note providing additional context about the
test or its scope.


Example 1: a metric with a FOOPS! test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The metric `FAIR Metric - A version IRI is declared in the ontology
metadata <https://doi.org/10.25504/FAIRsharing.99c9f7>`_ includes an
Associated Tests entry linking to a FOOPS! test. FOOPS! is an automated
tool for assessing the FAIRness of ontologies. In this case, the test
URL has been added directly by the metric maintainer rather than via
automated cross-referencing.

Opening the metric record and navigating to Additional Information >
Associated Tests will show you the FOOPS! test URL, from which you can
access the test itself and understand how it operationalises the metric.


Example 2: a metric with a FAIR Champion test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The metric `FAIR Metric - Metadata Contains CESSDA Provenance
Information <https://doi.org/10.25504/FAIRsharing.4e4752>`_ includes an
Associated Tests entry linking to a test registered in FAIR Champion at
`https://tools.ostrails.eu/champion/tests/
<https://tools.ostrails.eu/champion/tests/>`_.

FAIR Champion is a tool within the OSTrails ecosystem that registers and
executes FAIR tests. Opening the metric record and navigating to
Additional Information > Associated Tests will show you the FAIR
Champion test URL. Following that link takes you to the test record in
FAIR Champion, where you can view the test specification and, where
supported, execute it against a digital object.

.. note::

   If a metric record's Associated Tests field is empty, it does not
   necessarily mean that no test exists for that metric — it may not
   yet have been cross-referenced. You can search for tests directly
   in FAIR Champion at `https://tools.ostrails.eu/champion/tests/
   <https://tools.ostrails.eu/champion/tests/>`_, or contact the
   metric maintainer whose details appear in the record's General
   Information section.


Step 4: Follow the test URL
----------------------------

Once you have identified a test URL in the Associated Tests field,
follow it to access the test itself. For tests registered in FAIR Champion, the full list of available tests
is at `https://tools.ostrails.eu/champion/tests/
<https://tools.ostrails.eu/champion/tests/>`_.


Finding metrics that already have tests
-----------------------------------------

If you want to start from a list of metrics that are confirmed to have
at least one associated test, the following FAIRsharing advanced search
URL retrieves all Ready or In Development metrics with at least one
associated test:

`https://fairsharing.org/advancedsearch?operator=_and&fields=%28operator%3D_and%26fairassisttype%3Dmetric%26status%3Dready%2Bin_development%26associatedTests%3Dtrue%29 <https://fairsharing.org/advancedsearch?operator=_and&fields=%28operator%3D_and%26fairassisttype%3Dmetric%26status%3Dready%2Bin_development%26associatedTests%3Dtrue%29>`_

This is a practical starting point if you are building or evaluating a
FAIR assessment pipeline and want to work only with metrics that have
concrete implementations available.


Further reading
---------------

- :doc:`find-metrics-and-benchmarks` — how to discover metrics and
  benchmarks via FAIRassist and FAIRsharing.
- `FAIRsharing documentation on metric tests and examples
  <https://fairsharing.gitbook.io/fairsharing/additional-information/metric-tests-and-examples>`__
- `FAIRassist registry <https://fairassist.org/registry>`_
- `FAIR Champion test registry <https://tools.ostrails.eu/champion/tests/>`_

Finding a Test in FAIR Champion
-------------------------------
`FAIR Champion <https://tools.ostrails.eu/champion>`_ is a tool/framework designed to evaluate and assess digital objects based on FAIR metrics. More information can be found `here <https://github.com/markwilkinson/FAIR-Champion>`_.

FAIR Champion also allows you to discover FAIR Assessment Components, such as Tests, that are relevant to your needs.

Searching by keywords
---------------------
When accessing `its landing page <https://tools.ostrails.eu/champion>`_, FAIR Champion provides a set of links to different entries.
By clicking on the first option, *"List all Tests in OSTrails Registry"*, a browser interface will open, allowing you to search for Tests based on relevant terms.

You may want to look for a Test you previously identified using the FAIRassist tool (described in the previous section of this tutorial), or you can discover Tests from scratch if you do not already know their exact name.

1. Enter keywords related to your use case.
   The system will return a list of matching Tests based on their content, such as name and description.

2. Once you obtain the list of matching Tests, each result includes a short description to help you understand what the Test evaluates.
   You can use this information to quickly assess whether a Test is relevant to your needs.
   Additional information, such as the **Test ID** for the Benchmark Algorithm Spreadsheet, is available in the *Additional Details* drop-down.
   The option to run the Test is also available via the *Execute Test* drop-down.

Refining your search
--------------------
You can narrow down your results in two ways:

A. By refining your keywords to make them more specific.

B. By using FAIRassist beforehand to perform a more targeted search.
   This is especially useful if you have already identified a Test and want to locate it more quickly, while accessing its description, additional details, and execution options.

