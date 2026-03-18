======================
How to register a Metric
======================

This tutorial explains how to create a **community FAIR Metric** using the OSTrails FAIR Assessment framework.

A Metric is a narrative description that a Test must wholly implement. They may be domain-agnostic or not. 
For more information, check `the FAIR Testing Resource (FTR) vocabulary <https://ostrails.github.io/FAIR_testing_resource_vocabulary/release/1.2.0/index-en.html>`_. 

The process uses the `FAIR Wizard authoring tool <https://ostrails-fair.fair-wizard.com/wizard/dashboard>`_, a questionnaire-based knowledge model designed to collect and structure metadata for FAIR Assessment Components, including Metrics. It auto-generates FTR metadata and registers it in the appropriate registry or catalogue.


.. _metric_prerequisites:

Prerequisites
-------------

Before starting you should:

* Be familiar with the **FAIR Principles**.
* Have access to the `FAIR Wizard authoring tool <https://ostrails-fair.fair-wizard.com/wizard/dashboard>`_.
* Identify the **type of digital object** that your Metric will evaluate.

.. _create_project:

Step 1 – Create a Metric project in the FAIR Wizard authoring tool
--------------------------------------
1. Go to `the dedicated environment for this questionnaire <https://ostrails-fair.fair-wizard.com/wizard/>`_.
2. Register yourself or log in if you already have access.
3. Navigate to Projects and click Create to start a new project.
4. Name your project and use the "**FAIR Assessment Authoring Tool** - Questionnaire for creating FAIR Assessment Components" template as Knowledge Model.
5. Enable **Filter by question tags**.
6. Choose **Metric** as the artefact type. 

By doing this, the tool will create a Metric-tailored questionnaire.

.. _fill_out_questionnaire:

Step 2 – Fill in the questionnaire
--------------------------------------

1. Read the instructions carefully. 
2. Work through the form sequentially, completing each section with information relevant to the Metric you are defining. 

Note that there are questions that are *mandatory*, which will be required to be given an answer. Other questionas are optional. 
The mandatory fields that are required to define a FAIR Metric are:

- ``Title``
  You should indicate the title of your FAIR Assessment Component.

- ``Description``
  You should indicate a description of your FAIR Assessment Component.

- ``Abbreviation``
  You should indicate a single-word abbreviation for your FAIR Assessment Component. 

- ``License``
  You should include a license URL for this FAIR Assessment Component.

- ``Version``
  You should indicate the version number you are interested to use for defining your FAIR Assessment Component.

- ``Responsable contact person``
  You should provide the name and email of a responsible contact person. 

( - ``Other related FAIR assessment components``)
  This question might be optional or mandatory depending on the FAIR assessment component you are authoring. 


Step 3 – Create an instance with your answers
--------------------------------------

Once the questionnaire has been completed:

1. Go to the **Documents** section in the top menu.
2. Name your document and select the latest version of the "*FAIR Assessment Authoring Tool* - Jinja2-based template for authoring and registering FAIR Assessment Components" as Document Template.
3. Choose the "Metric / Benchmark" Format option. 
4. Click on *Create*.

This will create a JSON file with your input. 

Step 4 – Submit your document
--------------------------------------

Now, you can review the document with your answers to the questionnaire, by clicking on it, which will initiate the download of the file. Once you're happy with it, you're ready to submit your document:

4. In the **Documents** section, click the three dots icon (⋯) beside your document.
5. Select *Submit*.

The submission will be sent via the GitHub API to be registered in an OSTrails GitHub repository for collecting metadata about these assessment components <https://github.com/OSTrails/assessment-component-metadata-records>`_, and indexed by the `FAIRsharing <https://fairsharing.org/>`_ registry.


Next steps
----------








The form in the general information tab establishes the identity, ownership, and scientific scope of your record.
+-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Field | Status | Missing Fields Guidance | +=======================================================================================================================+=============+=======================================================================================================================================================================================================================+ | Record Name <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/record-name>_ | Mandatory | Provide the full name of the resource. You should create a name of the format: [[Principle name]] Metric - [[Abbreviation of sub-principle]] - [[Metadata or Data]] [[descriptive metric name]]. An example is “FAIR Metric – F1 – Metadata - Identifier is globally unique” | +-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Abbreviation <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/abbreviation>_ | Optional | You should create an abbreviation of the format: [[Principle abbrev]]M:[[Abbreviation of sub-principle]]:[[M or D]]:[[short name for the metric]]. An example is “FM:F1:M:IdentUnique” | +-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Homepage <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/homepage>_ | Mandatory | Provide the homepage URL for the resource.| +-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Description <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/description>_ | Mandatory | Free-text summary of the resource and its purpose; see also our documentation on descriptions. (Min. 40 chars) | +-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Year of creation <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/year-of-creation> | Recommended | Provide the year the resource was first released.| +-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Contacts <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/contact-information>_ | Mandatory | At least one contact point should be provided, consisting of a name and email address for the person or group responsible for the maintenance of the resource. | +-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Countries <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/countries>_ | Mandatory | Select the country or countries where the resource is hosted. At least one must be added. | +-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Subjects and Taxonomies <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/taxonomic-range-research-subjects-domains-and-user-defined-tags>_ | Mandatory | Select the relevant subject area and species. At least one of each must be added. “Not applicable” may be used for the Taxonomy value when the species is irrelevant, as is often the case for metrics. | +-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Object Type <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/object-types>_ | Mandatory | Define the type of digital research object in scope. At least one object type must be provided for Metrics/Benchmarks. | +-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**Licence and Support Links**
Ensures users understand how to access help and the legal usage rights of the metadata..
+-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Field | Status | Missing Fields Guidance | +=======================================================================================================================+=============+=======================================================================================================================================================================+ | Licences <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/licences-and-support-links/licences>_ | Recommended | Licences for the content of your resource (e.g. the specification) should be listed. Providing licences increases the likelihood of understanding usage rights. | +-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Support <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/licences-and-support-links/support-links>_ | Recommended | Support links allow you to supply information about the various types of documentation, training and support available for your resource. | +-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Publications**
Connects the record to the literature related to the metric.
+-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Field | Status | Missing Fields Guidance | +=======================================================================================================================+=============+=======================================================================================================================================================================+ | Publications <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/publications>_ | Recommended | This section is only for publications that describe your resource and those you would ask others to use when citing your database, standard or policy. | +-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Citations <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/publications#citing-your-resource>_ | Recommended | You may have one or more publications that should be used to cite your resource. Note this using the 'Cite record using this publication?' toggle. | +-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Organisations and Grants**
Defines the institutional backing and funding for the resource.
+-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Field | Status | Missing Fields Guidance | +=======================================================================================================================+=============+=======================================================================================================================================================================+ | Organisations <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/organisations-and-grants>_ | Recommended | Each organisation involved should be added with its role. At least one maintaining organisation and one funding organisation should be added. | +-----------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Relations to Other Records**
+-----------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | Field | Status | Specific Guidance & Help Text | +===================================================================================================================================+=============+===========================================================================================================================================================================================================================================================+ | related_to <https://fairsharing.gitbook.io/fairsharing/associated-records/from-fairassist-records>_ | Recommended | One of the most important parts of a record is its relationships. Link to records (other than benchmarks) via the autocomplete field using the FAIRsharing ID, full name, or short name. | +-----------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ | measures_principle <https://fairsharing.gitbook.io/fairsharing/associated-records/from-fairassist-records>_ | Mandatory | Every metric must be linked to exactly ONE principle record from any given principle hierarchy. Use for the narrowest principle possible (e.g. FAIR F1). Cannot point to two principles from the same hierarchy. | +-----------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Additional Information**

Specific functional metadata for assessment tools.
+-----------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------+ | Field | Status | Missing Fields Guidance | +===================================================================================================================================+=============+=========================================================================================================+ | Associated evaluation tools <https://fairsharing.gitbook.io/fairsharing/additional-information/associated-tools>_ | Optional | If your metric/benchmark is available from a particular FAIR evaluation tool, please add it here. | +-----------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------+ | Associated Tests <https://fairsharing.gitbook.io/fairsharing/additional-information/metric-tests-and-examples>_ | Optional |Links to the tests that execute this metric | 
+-----------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------+ | Positive, Negative and Indeterminate examples <https://fairsharing.gitbook.io/fairsharing/additional-information/metric-tests-and-examples#positive-examples>_ | Optional | URLs that provide illustrative examples of positive, negative and indeterminate outcomes | +-----------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------+










