Catalogue of Tests
==================

FAIR Data Point
---------------

OSTrails has generated a federated metadata registry for publishing and
indexing FAIR Test descriptions. Every test intended to be discoverable
and to support FAIR assessment activities should be registered in this
repository.

This repository is built on top of the **FAIR Data Point (FDP)**, a
software framework maintained by the
`FAIRDataTeam <https://github.com/FAIRDataTeam>`_.

.. figure:: Test-Algorithm-Registry.png
    :alt: Test Algorithm Registry
    :align: center

    Test Algorithm Registry


The FDP index includes descriptions of test records from multiple
assessment tools, such as
`FAIR Champion </docs/docs/tools/FAIR_tools/FAIR-Champion.rst>`_
and
`FOOPS </docs/docs/tools/FAIR_tools/FOOPS.rst>`_.

Registering a Test in the Catalogue
-----------------------------------

To register a test, you may use one of the following standardised
procedures:

Submitting an Existing Metadata Record via FAIR Champion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Visit the FAIR Champion registration page: https://tests.ostrails.eu/tests/new

Provide the persistent unique identifier of your existing metadata
record and submit it for indexing.

You may verify the publication and validation status of your metadata at: https://tools.ostrails.eu/fdp-index/

If your DCAT record contains structural or semantic errors, the metadata
may be displayed as **invalid**.


    NOTE: This method requires the metadata record to already exist in your
    tool or repository. The record **must** comply with the FTR model.

Registering Metadata via the FAIR Assessment Authoring Tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The FAIR Assessment Authoring Tool, developed by the OSTrails team,
supports the creation of FAIR assessment components such as Tests,
Metrics, Benchmarks, and others.

Through a machine-actionable questionnaire, the tool automatically
generates the metadata record, stores it, and submits it to an OSTrails
GitHub repository that acts as an openly accessible, self-hosted
index for transparency and long-term availability. This submission also
registers the record in the FDP-based OSTrails index: https://tools.ostrails.eu/fdp-index/

The FAIR Assessment Authoring Tool is available at: https://ostrails-fair.fair-wizard.com/wizard/dashboard

All its documentation is available `here </docs/docs/tools/FAIR_tools/FAIR-Assessment-Authoring-Tool.rst>`_
