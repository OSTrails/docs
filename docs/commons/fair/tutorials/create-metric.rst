How to create a Metric
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












