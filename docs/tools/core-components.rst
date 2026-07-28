.. _tool-core-components:

Core Components
================

The conceptual and code-level artefacts of the assessment space: Metrics and Benchmarks at the
conceptual level, Tests and Algorithms at the code level.

.. tip::

   This page covers several components. Use the **On this page** panel on the right to jump
   straight to a section.

.. _tool-conceptual-components:

Conceptual Components
----------------------

The conceptual components take the form of:

* *Metrics*: features of a digital object that can or should be measured, and why it is useful to measure them. These are instantiated as :ref:`Tests <tool-fair-tests>`.
* *Benchmarks*: overall expectations for the features of a digital object. Benchmarks are aggregations of Metrics, together with an explanation of how important a given metric is relative to other metrics, and how to interpret the pass/fail result of a metric or a group of metrics. These are instantiated as :ref:`Algorithms <tool-fair-algorithms>`.

.. _tool-fair-metrics:

FAIR Metrics
~~~~~~~~~~~~

.. raw:: html

   The metrics for FAIR testing are <a href="https://fairassist.org/registry?search=(recordType=metric_ids)" target="_blank" rel="noopener">catalogued in the FAIRassist repository</a> (hosted by FAIRsharing).

.. _tool-dmp-metrics:

DMP Metrics
~~~~~~~~~~~

.. raw:: html

    <a href="../commons/dmp/dmp-evaluation-metrics.html" target="_blank" rel="noopener">Open the catalogue of DMP Metrics</a>.

.. _tool-fair-benchmarks:

FAIR Benchmarks
~~~~~~~~~~~~~~~

.. raw:: html

   The community-authored benchmarks for FAIR assessment are
   <a href="https://fairassist.org/registry?search=(recordType=benchmark_ids)"
   target="_blank" rel="noopener">catalogued in the FAIRassist repository</a> (hosted by FAIRsharing).

.. _tool-code-components:

Code Components
-----------------

The code components take the form of:

* *Tests*: Tests are the code-level instantiations of the objectives defined by a :ref:`Metric <tool-fair-metrics>`.
* *Algorithms*: Algorithms are the code-level instantiations of the objectives and priorities defined by a :ref:`Benchmark <tool-fair-benchmarks>`.

FAIR Tests
~~~~~~~~~~

The tests below are maintained as live endpoints by the OSTrails project together with private partners who are committed to maintaining the testing infrastructure.
Tests are catalogued in the :ref:`OSTrails Software Tools Registry <software-registry>`, which provides the listing below via an API call.
All tests are compliant with the `FTR Vocabulary <https://w3id.org/ftr>`_ and can be executed through the platforms described under :ref:`tool-testing-platforms`.

The catalogue currently lists around 200 tests, so it is kept on its own searchable page:
:doc:`Browse the FAIR Tests catalogue <fair-tests>`.

.. _tool-dmp-tests:

DMP Tests
~~~~~~~~~

DMP Tests are listed in the `catalogue of DMP Tests <../commons/dmp/dmp-catalogue-of-tests.html>`_.
These are not maintained as "live" endpoints; rather, users are invited to select the tests of
interest to them and deploy them on their own infrastructure.

FAIR Algorithms
~~~~~~~~~~~~~~~~

The algorithms below are maintained as live endpoints by the OSTrails project together with private partners who are committed to maintaining the testing infrastructure.
Algorithms are catalogued in the :ref:`OSTrails Software Tools Registry <software-registry>`, which provides the listing below via an API call.
All algorithms are compliant with the `FTR Vocabulary <https://w3id.org/ftr>`_ and can be executed through the platforms described under :ref:`tool-testing-platforms`.

The catalogue currently lists about a dozen algorithms, so it is kept on its own searchable page:
:doc:`Browse the FAIR Algorithms catalogue <fair-algorithms>`.
