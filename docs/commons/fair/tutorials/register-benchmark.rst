
======================
How to register a Benchmark
======================

This tutorial explains how to register a **community FAIR Benchmark** using the OSTrails FAIR Assessment framework.

A Benchmark is a community-specific grouping of a set of Metrics that provides a narrative of those particular ways in which that community defines FAIR for assessment purposes. 
For more information, check `the FAIR Testing Resource (FTR) vocabulary <https://ostrails.github.io/FAIR_testing_resource_vocabulary/release/1.2.0/index-en.html>`_. 

There are two ways to register a Benchmark. The first is to use the `FAIR Wizard authoring tool <https://ostrails-fair.fair-wizard.com/wizard/dashboard>`_, a questionnaire-based knowledge model designed to collect and structure metadata for FAIR Assessment Components, including Benchmarks. It auto-generates FTR metadata and registers it in FAIRsharing for you. The second is to register your Benchmark directly with FAIRsharing. This tutorial covers both options.

FAIR Wizard
======================

.. _metric_prerequisites:

Prerequisites
-------------

Before starting you should:

* Have a defined set of **FAIR Metrics**, as well as any required **community-specific specialised Metrics**. You may find the tutorial at `define-benchmark-associated-metrics.rst <https://github.com/OSTrails/assessment-component-metadata-records/blob/bd0b3b9aaae4e1c2138904c4d90a609f784e10bc/README.md>`_ useful.
* Have a completed **community FAIR Benchmark narrative** definition, aligned with the community or discipline for which it will apply. This can be done by following the tutorial at  `define-benchmark-associated-metrics.rst <https://github.com/OSTrails/assessment-component-metadata-records/blob/bd0b3b9aaae4e1c2138904c4d90a609f784e10bc/README.md>`_. This narrative definition of FAIR will contain a description of your benchmark
* Have access to the `FAIR Wizard authoring tool <https://ostrails-fair.fair-wizard.com/wizard/dashboard>`_.

.. _create_project:

Step 1 – Create a Benchmark project in the FAIR Wizard authoring tool
--------------------------------------
1. Go to `the dedicated environment for this questionnaire <https://ostrails-fair.fair-wizard.com/wizard/>`_.
2. Register yourself or log in if you already have access.
3. Navigate to Projects and click Create to start a new project.
4. Name your project and use the "**FAIR Assessment Authoring Tool** - Questionnaire for creating FAIR Assessment Components" template as Knowledge Model.
5. Enable **Filter by question tags**.
6. Choose **Benchmark** as the artefact type. 

By doing this, the tool will create a Benchmark-tailored questionnaire.

.. _fill_out_questionnaire:

Step 2 – Fill in the questionnaire
--------------------------------------

1. Read the instructions carefully. 
2. Work through the form sequentially, completing each section with information relevant to the Benchmark you are defining. 

Note that there are questions that are *mandatory*, which will be required to be given an answer. Other questions are optional. 
The mandatory fields that are required to define a FAIR Benchmark are:

- ``Title`` 
You should indicate the title of your Benchmark. To follow OSTrails best practices, consider using this Benchmark naming scheme: [[Principles name]] Benchmark - [[descriptive benchmark name]] 


Examples:

 FAIR Benchmark - Assessment of Repositories and Knowledgebases (https://fairsharing.org/7162)  
 
 FAIR4RS Benchmark - General Benchmark for RSFC (https://fairsharing.org/7056)  
 
 FAIR Benchmark - CESSDA Data Catalogue (CDC) 

- ``Description`` 
You should indicate a description of your Benchmark.

- ``Abbreviation`` 
You should indicate a single-word abbreviation for your Metric. Note that FAIR Wizard does not allow the use of spaces or any of these special characters in Benchmark/Metric/Test name abbreviations: : / ? # [ ] @ ! $ & ' ( ) * + , ; = "< > \ ^ { < > : " / \
To follow OSTrails best practices, consider using this Metric naming scheme: 
[[Principle abbrev]]B - [[short name for the benchmark]] 
 
Examples:

 FB - ARK 

 FSB - RSFC 
 
 FB - CESSDA   

- ``License`` 
You should  include a license URL for this Benchmark. Please do not include angle brackets "<>" in your response.

- ``Version`` 
You should indicate the version number you are interested in using for defining your Benchmark. 

- ``Organisation information`` 
This question is mandatory for FAIRsharing submission. Your Benchmark might be associated with an institution as its creator or maintainer.

- ``Responsable contact person`` 
You should provide the name and email of a responsible contact person. You will find an ORCID-integrated browser to search for your personal information by either typing in your full name or your ORCID ID directly.

- ``Country`` 
You should indicate the country or geographical scope relevant to this Benchmark. If the Benchmark is not limited to a specific region, you can select *‘Worldwide’*.

- ``Subject`` 
You should specify the application domain or area of knowledge to which the Benchmark applies. If the Metric is intended to be domain-independent, you can select *‘Subject Agnostic’*.

- ``Object type`` 
You should indicate the type of digital object that the Benchmark evaluates (for example datasets, software, or workflows). If the Benchmark applies broadly, you can select Object type *’Agnostic’*.

- ``Taxonomy`` 
You should classify the Benchmark within a taxonomy. If no suitable classification is available or needed, you can select *’Not Applicable’*.

- ``Link to a Metric`` 
You should link the Benchmark to at least one Metric. Use this relationship to link to every Metric implemented by this Benchmark: `has_associated_metric <https://fairsharing.gitbook.io/fairsharing/associated-records/from-fairassist-records>`_.

- ``Other related FAIR assessment components`` 
This question might be optional or mandatory depending on the FAIR assessment component you are authoring. For Benchmarks, this question is mandatory, as it needs to have associated Metrics. 



**Please complete all optional sections that it is possible for you to complete. The more complete your metric, the more re-usable and FAIR it is. Incomplete metadata may delay the publishing of your Benchmark in FAIRsharing.**


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

The submission will be sent via the GitHub API to be registered in an `OSTrails GitHub repository for collecting metadata about these assessment components <https://github.com/OSTrails/assessment-component-metadata-records>`_, and indexed by the `FAIRsharing <https://fairsharing.org/>`_ registry.


Next steps
----------

Once submitted to FAIRsharing, the record will remain hidden until approved by the FAIRsharing curation team. Once made public, claim your record in FAIRsharing. Information on creating an account and claiming a record is available in the next section, and at `fairsharing.gitbook.io <https://fairsharing.gitbook.io/>`_.


FAIRsharing
======================

This tutorial provides a comprehensive walkthrough for registering a **Benchmark** directly within the FAIRassist registry on FAIRsharing.

Prerequisites
-------------
* Ensure you are logged in via your ORCID. This ensures your curation work is publicly attributed to you. You can find out more about creating an account in our `gitbook documentation <https://fairsharing.gitbook.io/fairsharing#accessing-fairsharing-through-3rd-party-accounts>`_.
* Create a narrative description of your benchmark, and how it interprets the `FAIR Principles <https://doi.org/10.1038/sdata.2016.18>`_. You may find the benchmark sections of the tutorial at `define-benchmark-associated-metrics.rst <https://github.com/OSTrails/assessment-component-metadata-records/blob/bd0b3b9aaae4e1c2138904c4d90a609f784e10bc/README.md>`_ useful. 

Creating a record
----------------
Please follow the instructions in `our documentation <https://fairsharing.gitbook.io/fairsharing#creating-a-record>`_ on how to create a new record in FAIRsharing. Once you’ve done that, you will be presented with the more detailed record edit interface.

Editing your record
----------------

Each of the tables below corresponds to a single tab of the edit interface for a FAIRsharing record, and summarises the key fields that should be populated. For complete documentation, see our `gitbook pages <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/how-to-update-a-record>`_.

Remember to save your record regularly.

General Information
===================

The form in the general information tab establishes the identity, ownership, and scientific scope of your record.

* `Record Name <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/record-name>`_ (Mandatory): Provide the full name of the resource. You should create a name of the format: [[Principle name]] Benchmark - [[descriptive benchmark name]]. An example is “FAIR Benchmark - FAIR Portugal Dataverse Benchmark”.
* `Abbreviation <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/abbreviation>`_ (Optional): You should create an abbreviation of the format: [[Principle abbrev]]B:[[short name for the benchmark]]. An example is “FB - FAIR PT-DV”.
* `Homepage <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/homepage>`_ (Mandatory): Provide the homepage URL for the resource.
* `Description <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/description>`_ (Mandatory): Free-text summary of the resource and its purpose; see also our documentation on descriptions. (Min. 40 chars).
* `Year of creation <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/year-of-creation>`_ (Recommended): Provide the year the resource was first released.
* `Contacts <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/contact-information>`_ (Mandatory): At least one contact point should be provided, consisting of a name and email address for the person or group responsible for the maintenance of the resource.
* `Countries <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/countries>`_ (Mandatory): Select the country or countries where the resource is hosted. At least one must be added.
* `Subjects and Taxonomies <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/taxonomic-range-research-subjects-domains-and-user-defined-tags>`_ (Mandatory): Select the relevant subject area and species. At least one of each must be added. “Not applicable” may be used for the Taxonomy value when the species is irrelevant, as is often the case for benchmarks.
* `Object Type <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/object-types>`_ (Mandatory): Define the type of digital research object in scope. At least one object type must be provided for Metrics/Benchmarks.

Licence and Support Links
=========================

Ensures users understand how to access help and the legal usage rights of the metadata.

* `Licences <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/licences-and-support-links/licences>`_ (Recommended): Licences for the content of your resource (e.g. the specification) should be listed. Providing licences increases the likelihood of understanding usage rights.
* `Support <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/licences-and-support-links/support-links>`_ (Recommended): Support links allow you to supply information about the various types of documentation, training and support available for your resource.

Publications
============

Connects the record to the literature related to the benchmark.

* `Publications <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/publications>`_ (Recommended): This section is only for publications that describe your resource and those you would ask others to use when citing your database, standard or policy.
* `Citations <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/publications#citing-your-resource>`_ (Recommended): You may have one or more publications that should be used to cite your resource. Note this using the 'Cite record using this publication?' toggle.

Organisations and Grants
========================

Defines the institutional backing and funding for the resource.

* `Organisations <https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/organisations-and-grants>`_ (Recommended): Each organisation involved should be added with its role. At least one maintaining organisation and one funding organisation should be added.

Relations to Other Records
==========================

* `related_to <https://fairsharing.gitbook.io/fairsharing/associated-records/from-fairassist-records>`_ (Recommended): One of the most important parts of a record is its relationships. Link to records (other than metrics) via the autocomplete field using the FAIRsharing ID, full name, or short name.
* `has_associated_metric <https://fairsharing.gitbook.io/fairsharing/associated-records/from-fairassist-records>`_ (Mandatory): Use this relationship to link to every metric implemented by this benchmark.

Additional Information
======================

Specific functional metadata for assessment tools.

* `Associated evaluation tools <https://fairsharing.gitbook.io/fairsharing/additional-information/associated-tools>`_ (Optional): If your metric/benchmark is available from a particular FAIR evaluation tool, please add it here.
