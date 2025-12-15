FAIR Assessment Authoring Tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A complete framework for **generating, registering, and authoring your FAIR assessment components** across different metadata repositories.

The different FAIR assessment metadata components:

* FAIR Benchmark
* FAIR Metric
* FAIR Test
* FAIR Benchmark Algorithm

Authoring workflow
------------------

The FAIR Assessment Authoring Tool integrates **three main steps**:

1. **FAIR Wizard Knowledge Model**

   A questionnaire-based knowledge model for capturing your metadata fields using machine-actionable questions.  
   It connects via APIs to various registries, such as `ORCID <https://orcid.org>`_, `ROR <https://ror.org>`_, and `FAIRsharing <https://fairsharing.org>`_.

2. **DSW-TDK-based Template Transformation**

   DSW-TDK templates transform your questionnaire data into different serializations, such as JSON and RDF (Turtle).

3. **Proxy Submission Service**

   Registers your generated metadata into the appropriate repository or registry, authoring your FAIR metadata automatically.

Submissions
~~~~~~~~~~~

The following table summarises the available submission options:

+-----------------------+----------------+----------------------------+----------------------------------------------+
| **Registries**        | **Format**     | **Submission Method**      | **Assessment Components**                    |
+=======================+================+============================+==============================================+
| FAIRsharing Record    | JSON           | FAIRsharing Registry       | Benchmarks and Metrics                       |
+-----------------------+----------------+----------------------------+----------------------------------------------+
| DCAT Record           | RDF (Turtle)   | GitHub / FAIR Data Point   | Benchmarks, Metrics, Tests, Scoring          |
|                       |                |                            | Algorithms                                   |
+-----------------------+----------------+----------------------------+----------------------------------------------+
| FDP Test Record       | RDF (Turtle)   | GitHub / FAIR Data Point   | Tests                                        |
+-----------------------+----------------+----------------------------+----------------------------------------------+


Step-by-Step Guide
------------------

1. Fill in the Questionnaire
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to the dedicated environment for this questionnaire:  
   https://ostrails-fair.fair-wizard.com/wizard/
2. Register yourself or log in if you already have access.
3. Navigate to **Projects** and click **Create** to start a new project.  
   Each project corresponds to one FAIR assessment component.
4. Give your project a **name** and select the **filter** corresponding to the specific type of assessment component you want to create.

2. Template Your Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Populate your metadata using the **machine-actionable questionnaire**.
2. Once all desired fields are completed, click **Documents** in the top menu.
3. Create an instance of your completed questionnaire by selecting the latest version of the **FAIR Assessment Authoring Tool Template**.
4. Choose your preferred **serialization format**:

   * **JSON** – for registration in FAIRsharing  
   * **Turtle (RDF)** – for generating a DCAT-compliant record

3. Submit Your Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

Once your document is generated, you can review it or submit it directly using the tool’s **submission service**.

1. In the **Documents** section, click the three dots icon (⋯) beside your document.
2. Select **Submit**.

Depending on your document format:

* If your record is formatted in **JSON**, the submission will be sent via the FAIRsharing API to be authored at their registry.

  .. note::

     *Why Use This Tool?*  
     FAIR assessment components are a specific subtype of records within the FAIRsharing registry.  
     Using this tool significantly reduces manual curation and accelerates the registration process.

* If your record is formatted in **Turtle**, the submission will be sent via the GitHub API to be registered in an OSTrails GitHub repository for collecting metadata about these assessment components.

If your assessment component is a **FAIR Test**, this submission will also register the test in the  
`OSTrails FAIR Data Point test index <https://tools.ostrails.eu/fdp-index/>`_.

References
----------

* `DCAT Vocabulary (W3C) <https://www.w3.org/TR/vocab-dcat-3/>`_
* `FAIR Testing Resource (FTR) <https://ostrails.github.io/FAIR_testing_resource_vocabulary/release/1.2.0/index-en.html>`_
* `DSW-TDK Github template repository <https://github.com/OSTrails/dsw-tdk-authoring-tool-template>`_
* `Proxy service Github repository <https://github.com/pabloalarconm/proxy-service-authoring-tool>`_
* `Proxy service endpoint <https://tools.ostrails.eu/questionnaire/docs>`_
* `FAIRsharing API documentation <https://fairsharing.org/API_doc>`_

Contact us
----------

Any question or issue related to this workflow, please contact:  
``pablo.alarcon@upm.es``
