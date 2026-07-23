.. _tool-supporting-tools:

Supporting Tools
=================

Tools that support authoring, registration, validation, and quality control of FAIR assessment
components.

.. tip::

   This page covers several tools. Use the **On this page** panel on the right to jump
   straight to one.

Assessment Authoring and Registration Tools
----------------------------------------------

.. _tool-fair-assessment-authoring-tool:

FAIR Assessment Authoring Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A complete framework for **generating, registering, and authoring your FAIR assessment components** across different metadata repositories.

The different FAIR assessment metadata components:

* FAIR Benchmark
* FAIR Metric
* FAIR Test
* FAIR Benchmark Algorithm

Authoring workflow
^^^^^^^^^^^^^^^^^^^

The FAIR Assessment Authoring Tool integrates **three main steps**:

1. **FAIR Wizard Knowledge Model**

    A questionnaire-based knowledge model for capturing your metadata fields using machine-actionable questions.
    It connects via APIs to various registries, such as `ORCID <https://orcid.org>`_, `ROR <https://ror.org>`_, and `FAIRsharing <https://fairsharing.org>`_.

2. **DSW-TDK-based Template Transformation**

    DSW-TDK templates transform your questionnaire data into different serializations, such as JSON and RDF (Turtle).

3. **Proxy Submission Service**

    Registers your generated metadata into the appropriate repository or registry, authoring your FAIR metadata automatically.

Submissions
""""""""""""

The following table summarises the available submission options:

+------------------------+----------------+----------------------------+--------------------------------------------+
| **Registries**         | **Format**     | **Submission Method**      | **Assessment Components**                  |
+========================+================+============================+============================================+
| FAIRsharing Record     | JSON           | FAIRsharing Registry       | Benchmarks and Metrics                     |
+------------------------+----------------+----------------------------+--------------------------------------------+
| DCAT Record            | RDF (Turtle)   | GitHub / FAIR Data Point   | Benchmarks, Metrics, Tests, Scoring        |
|                        |                |                            | Algorithms                                 |
+------------------------+----------------+----------------------------+--------------------------------------------+
| FDP Test Record        | RDF (Turtle)   | GitHub / FAIR Data Point   | Tests                                      |
+------------------------+----------------+----------------------------+--------------------------------------------+

Step-by-Step Guide
^^^^^^^^^^^^^^^^^^^

1. Fill in the Questionnaire
""""""""""""""""""""""""""""

1. Go to the dedicated environment for this questionnaire:
   https://ostrails-fair.fair-wizard.com/wizard/
2. Register yourself or log in if you already have access.
3. Navigate to **Projects** and click **Create** to start a new project.
   Each project corresponds to one FAIR assessment component.
4. Give your project a **name** and select the **filter** corresponding to the specific type of assessment component you want to create.

2. Template Your Information
""""""""""""""""""""""""""""

1. Populate your metadata using the **machine-actionable questionnaire**.
2. Once all desired fields are completed, click **Documents** in the top menu.
3. Create an instance of your completed questionnaire by selecting the latest version of the **FAIR Assessment Authoring Tool Template**.
4. Choose your preferred **serialization format**:

   * **JSON** – for registration in FAIRsharing
   * **Turtle (RDF)** – for generating a DCAT-compliant record

3. Submit Your Information
""""""""""""""""""""""""""

Once your document is generated, you can review it or submit it directly using the tool's **submission service**.

1. In the **Documents** section, click the three dots icon (⋯) beside your document.
2. Select **Submit**.

Depending on your document format:

* If your record is formatted in **JSON**, the submission will be sent via the FAIRsharing API to be authored at their registry.

  .. note::

     *Why use this tool?*
     FAIR assessment components are a specific subtype of records within the FAIRsharing registry.
     Using this tool significantly reduces manual curation and accelerates the registration process.

* If your record is formatted in **Turtle**, the submission will be sent via the GitHub API to be registered in an OSTrails GitHub repository for collecting metadata about these assessment components.

If your assessment component is a **FAIR Test**, this submission will also register the test in the
`OSTrails FAIR Data Point test index <https://tools.ostrails.eu/fdp-index/>`_.

References
^^^^^^^^^^

    * `DCAT Vocabulary (W3C) <https://www.w3.org/TR/vocab-dcat-3/>`_
    * `FAIR Testing Resource (FTR) <https://ostrails.github.io/FAIR_testing_resource_vocabulary/release/1.2.0/index-en.html>`_
    * `DSW-TDK GitHub template repository <https://github.com/OSTrails/dsw-tdk-authoring-tool-template>`_
    * `Proxy service GitHub repository <https://github.com/pabloalarconm/proxy-service-authoring-tool>`_
    * `Proxy service endpoint <https://tools.ostrails.eu/questionnaire/docs>`_
    * `FAIRsharing API documentation <https://fairsharing.org/API_doc>`_

Contact us
^^^^^^^^^^

For any question or issue related to this workflow, please contact ``pablo.alarcon@upm.es``.

Validation and Quality Control Tools
----------------------------------------

.. _tool-openaire-validator:

OpenAIRE Metadata Validator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The OpenAIRE Metadata Validator is a software tool that evaluates metadata records of research products (publications, datasets, software, and other outputs) against the OpenAIRE Guidelines, which set the minimum requirements for inclusion in the OpenAIRE Graph. Building on this compliance assessment, the tool is being extended with FAIR evaluation capabilities through the FAIR Validator. The version presented here implements the FAIR Reference Model defined by OSTrails and provides a user interface for running both the OpenAIRE Guidelines and FAIR assessments. The release also includes the source code of the OSTrails API tool.

- **Persistent identifier**: https://beta.validator.openaire.eu
- **Code repositories**:

  - https://code-repo.d4science.org/MaDgIK/metadata-validator-ui
  - https://code-repo.d4science.org/MaDgIK/uoa-validator-api
  - https://code-repo.d4science.org/MaDgIK/openaire-ostrails-api
  - https://code-repo.d4science.org/MaDgIK/uoa-validator-engine2

- **Version**: Release v1.2.0
- **Releases**:

  - https://code-repo.d4science.org/MaDgIK/metadata-validator-ui/releases/tag/1.2.0
  - https://code-repo.d4science.org/MaDgIK/uoa-validator-api/releases/tag/1.2.0
  - https://code-repo.d4science.org/MaDgIK/openaire-ostrails-api/releases/tag/1.2.0
  - https://code-repo.d4science.org/MaDgIK/uoa-validator-engine2/releases/tag/v3.0.0

- **API documentation (Swagger)**: `Swagger UI <https://beta.services.openaire.eu/osTrails/swagger-ui/index.html#/>`_
- **API endpoints**:

  - https://beta.services.openaire.eu/osTrails/forms/benchmarks
  - https://beta.services.openaire.eu/osTrails/forms/metrics
  - https://beta.services.openaire.eu/osTrails/forms/tests

- **License**: Apache-2.0

.. _tool-ftr-validator:

FAIR FTR Schema Validator
~~~~~~~~~~~~~~~~~~~~~~~~~~

FTR includes `ShEX and SHACL files <https://github.com/OSTrails/FAIR_testing_resource_vocabulary/tree/main/development>`_
for the different assessment components, allowing you to validate your
FTR records against this representation using any RDF validator tool,
such as `rudof <https://rudof-project.github.io/>`_.

A dedicated `FastAPI-based validation service <https://github.com/pabloalarconm/FAIR-assessment-record-validator>`_
is also available, wrapping **rudof** and exposing endpoints per entity type (``test``, ``testResult``,
``testResultSet``, ``metric``, ``benchmark``) and format (TTL or JSON-LD),
returning a structured validation report. It is fully containerized and ready to run with Docker.

    - **Persistent identifier**: not available yet
    - **Code repository**: https://github.com/pabloalarconm/FAIR-assessment-record-validator
    - **Version**: v0.3.0
    - **Release**: https://hub.docker.com/layers/pabloalarconm/fair-assessment-record-validator/0.3.0/
    - **License**: CC0 1.0 Universal

.. _tool-skg-api-validator:

SKG API Validator
~~~~~~~~~~~~~~~~~~

To validate that an implementation aligns with an OpenAPI specification contract, API implementers can use
`PRISM <https://docs.stoplight.io/docs/prism/>`_, a validation proxy. The SKG-IF API documentation provides
guidance on using this tool (see https://skg-if.github.io/api/).

    - **Persistent identifier**: not available yet
    - **Code repository**: https://github.com/stoplightio/prism
    - **Version**: 5.15.11
    - **Release**: https://github.com/stoplightio/prism/releases/tag/v5.15.11
    - **License**: Apache-2.0
