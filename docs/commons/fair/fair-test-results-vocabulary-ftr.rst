FAIR Testing Resource Vocabulary (FTR)
=======================================

Definition
----------

The FAIR Testing Resource Vocabulary (FTR) is an ontology created to
describe the results of FAIR Assessment in a consistent,
machine-readable way. Its purpose is to help different FAIR assessment
tools communicate the same language for transparency and reusability.

FTR is the **application profile** of the assessment components,
acting as a reference model that extends W3C standards such as
`DCAT <https://www.w3.org/TR/vocab-dcat-3/>`_,
`DQV <https://www.w3.org/TR/vocab-dqv/>`_,
`PROV <https://www.w3.org/TR/prov-o/>`_,
and others to describe the different assessment components, such as:

- **Test**: Service, formed by an API and associated piece of code that implements a Metric, and is executed (by a FAIR assessment tool), retrieving a particular and standardised result.
- **TestResult**: Output of running a test over a resource. A test result should also contain provenance metadata about the process followed to create it. ``TestResult`` is represented as an extension of ``prov:Entity``. A test result points to the corresponding test through the ``ftr:outputFromTest`` property.
- **TestResultSet**: A set of FAIR test results, together with their respective metadata. Common metadata may describe the set. For example, if all results were run by a request to the same API.
- **TestExecutionActivity**: The action carried out by an agent

calling an API in which a test (or set of tests) was run. The result
of this activity is either a ``TestResult`` or a ``TestResultSet``.

- **Metric**: Narrative domain-agnostic description that a Test must wholly implement.
- **Benchmark**: Community-specific groupings of a set of Metrics that provide a narrative describing how that community defines FAIR for assessment purposes.
- **ScoringAlgorithm**: Piece of code that contextualises the sum of all test results for a given benchmark into a final quantitative assessment result.
- **ScoringAlgorithmActivity**: The action carried out by an agent calling an API in which a ``ScoringAlgorithm`` was executed. The result of this activity is a ``BenchmarkScore``.
- **BenchmarkScore**: Output of a Scoring Algorithm over a resource, generating the final score and guidance for the whole assessment.

----

.. figure:: fair-test-results-vocabulary-ftr-diagram.png
    :alt: FAIR Testing Resource Vocabulary (FTR)
    :target: https://github.com/OSTrails/FAIR_testing_resource_vocabulary


Specification
-------------

    * The full FAIR Testing Resource Vocabulary (FTR) 1.2.0 is specified here: https://w3id.org/ftr/1.2.0

    * You can also explore the GitHub repository for additional content: https://github.com/OSTrails/FAIR_assessment_output_specification/


FAIR assessment validation
--------------------------
:doc:`FAIR assessment validation <tools/quality-control/ftr-validator>`
