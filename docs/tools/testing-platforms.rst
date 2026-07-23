.. _tool-testing-platforms:

Testing Platforms
==================

The assessment platforms that execute FAIR and DMP tests against digital objects.

.. contents:: On this page
    :local:
    :depth: 2

FAIR Assessment Platforms
---------------------------

These are the assessment platforms that provide users with access to :ref:`Tests and Algorithms <tool-code-components>`.

.. _tool-fair-champion:

FAIR Champion
~~~~~~~~~~~~~

FAIR Champion is a general-purpose FAIR assessment tool intended to be used by all communities and for all digital objects. In this release, FAIR Champion is aware of the 22 FAIR Tests described under :ref:`tool-fair-tests`, but any test, from any provider, can be registered so long as the test generates a metadata descriptor compliant with the FAIR Reference Model defined by OSTrails. The OpenAPI interface descriptor for this release is only partially complete; the Champion has a variety of functions related to new test registration and benchmark registration that are currently pending decisions by the OSTrails project.

    - **Persistent identifier**: https://w3id.org/FAIR-Champion
    - **Code repository**: https://github.com/OSTrails/FAIR-Champion
    - **Version**: Release v2.0.0
    - **Release**: https://github.com/OSTrails/FAIR-Champion/releases/tag/2.0.0
    - **License**: MIT

.. _tool-foops:

FOOPS!
~~~~~~

The Ontology Pitfall Scanner for FAIR (FOOPS!) is a FAIR assessment tool for vocabularies and ontologies. In this release, FOOPS! has been adapted to comply with the `FTR specification <https://w3id.org/ftr/>`_. A `catalog of test descriptions and metrics <https://w3id.org/foops/catalogue>`_ has been made available. The release contains the source code of the tool, as well as the machine-readable and human-readable documentation of all tests, metrics, and benchmarks associated with the tool.

    - **Persistent identifier**: https://w3id.org/foops/
    - **Zenodo link (latest release)**: https://doi.org/10.5281/zenodo.14767999
    - **Code repository**: https://github.com/oeg-upm/fair_ontologies
    - **Version**: 0.2.0
    - **Release**: https://github.com/oeg-upm/fair_ontologies/releases/tag/v0.2.0
    - **License**: Apache-2.0
    - **Catalog of tests and metrics**: https://w3id.org/foops/catalogue

.. _tool-fairos:

FAIROS
~~~~~~

FAIROS is a FAIR assessment tool for `Research Objects <https://www.researchobject.org/ro-crate/>`_. The tool uses external tools such as `F-UJI <https://f-uji.net/>`_, `FOOPS <https://w3id.org/foops/>`_, and `RSFC <https://github.com/oeg-upm/rsfc>`_ to assess datasets, ontologies, and software. The catalog contains the metrics and tests used to evaluate Research Objects. The source code with the FTR specification is in the ``dev-ostrails`` branch.

    - **Persistent identifier**: https://w3id.org/FAIROS/
    - **Zenodo link (latest release)**: https://doi.org/10.5281/zenodo.7795727
    - **Code repository**: https://github.com/oeg-upm/FAIR-Research-Object
    - **Version**: 0.0.2
    - **Release**: https://github.com/oeg-upm/FAIR-Research-Object/releases/tag/v0.0.2
    - **License**: Apache-2.0
    - **Test and metric catalogue**: https://w3id.org/FAIROS/catalog

.. _tool-rsfc:

RSFC
~~~~

RSFC (Research Software FAIRness Checks) is a tool designed to evaluate how well a research software repository complies with the FAIR principles (Findable, Accessible, Interoperable, and Reusable).

    - **Persistent identifier**: https://w3id.org/rsfc/
    - **Zenodo link (latest release)**: https://doi.org/10.5281/zenodo.19554471
    - **Code repository**: https://github.com/oeg-upm/rsfc
    - **Version**: 0.1.5
    - **Release**: https://github.com/oeg-upm/rsfc/releases/tag/v0.1.5
    - **License**: MIT
    - **Catalog of tests and metrics**: https://w3id.org/rsfc/catalogue

.. _tool-pyfat:

pyFAT
~~~~~

pyFAT is a FAIR assessment tool that was originally developed under CLARIAH-NL. It was recently updated to be compliant with the FAIR Reference Model defined by OSTrails. It adheres to the FAIR Testing Resource Vocabulary (`FTR <https://w3id.org/ftr#>`_) and FAIR Guidance Vocabulary (`FGV <https://w3id.org/fgv#>`_) ontologies developed within OSTrails. It uses path expressions to traverse metadata records and perform the assessment. The metrics and tests are never hardcoded in pyFAT itself, so it is possible to specify tests for any metadata format. Currently, it is set up to test metadata records formatted in CLARIN's Component Metadata Infrastructure (CMDI).

In this release, which is still in beta, pyFAT is able to register tests in FAIR Champion, because the test generates a metadata descriptor compliant with the FAIR Reference Model defined by OSTrails.

    - **Code repository**: https://github.com/knaw-huc/ost-pyfat-api
    - **Version**: Release v0.1
    - **Release**: https://pyfat.sd.di.huc.knaw.nl/docs#
    - **License**: MIT

DMP Assessment Platforms
---------------------------

.. _tool-dmp-platforms:

DAMAP, DSWizard, and Argos are Data Management Plan (DMP) platforms that work towards implementing the DMP Common Standard (DMP-IF). These tools adopt and use the common concepts, structures, and conventions described in this documentation to enable interoperability and exchange of DMP information. For tool-specific functionality, implementation details, or support related to DMP-IF, please contact the respective tool providers directly.

    - **DAMAP**: https://damap.org/
    - **DSWizard**: https://ds-wizard.org/
    - **Argos**: https://argos.openaire.eu/portal/
