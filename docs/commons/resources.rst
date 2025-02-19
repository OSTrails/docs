OSTrails Commons: Resources
===========================

.. page-authors::
    Daniel Garijo
    Marek Suchánek


This page embodies the OSTrails Commons, a collection of reusable resource according to its structure as :ref:`components <commons-structure>`.

DMP Commons
-----------

The following resources in this section are part of the DMP Commons component.

OSTrails Application Profile for maDMPs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OSTrails Application Profile (AP) as a tailored extension of the `RDA DMP Common Standard (DCS) for maDMPs <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard>`_ will be designed to enhance interoperability while addressing various requirements (e.g. funders). Technically, the specification of the application profile will be done as prescribed by the DCS (which will support such extensions) and will be part of the Commons as the description of data structure.

- *Planned resource to be developed*


OSTrails maDMP API Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

maDMP API Specification will build on top of the DSC and OSTrails AP and specify the operations and data exchange. We plan to materialize this in the form of OpenAPI specification (using the current version, currently v3.1.1. Again, this promotes adoption as OpenAPI specification not only documents the API but also provides a way to generate source code or other artifacts (e.g. tests) as well as check compliance.

- *Planned resource to be developed*


SKG Commons
-----------

The following resources in this section are part of the SKG Commons component.

OSTrails SKG IF
^^^^^^^^^^^^^^^

OSTrails SGK-IF as an extension of the `RDA SKG-IF <https://skg-if.github.io/>`_ will focus on Common Standard and Data Model extensions, resulting in a specification for data structures guiding the adoption.

- *Planned resource to be developed*


OSTrails SKG-IF Common API
^^^^^^^^^^^^^^^^^^^^^^^^^^

SKG-IF Common API will be a specification of API following identified use cases and supporting relevant operators to guide the adoption and eventually also check compliance.

- *Planned resource to be developed*


FAIR Commons
------------

The following resources in this section are part of the FAIR Commons component.

FAIR Assessment specifications and SHACL shapes (FTR)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FTR is the first OWL implementation of the FAIR Reference model described in Deliverables D1.2 and D.1.4. The reference model extends W3C standards such as DCAT (https://www.w3.org/TR/vocab-dcat-3/), DQV (https://www.w3.org/TR/vocab-dqv/) and PROV (https://www.w3.org/TR/prov-o/) to describe test results, test definitions, metrics, benchmarks, algorithms, dimensions/principles and their interpretation to generate a FAIR assessment score.

The code release includes the vocabularies, definitions, specifications in machine-readable format and a set of SHACL validation rules to ensure tests and metrics are defined according to the specification.

- Persistent identifier: https://w3id.org/ftr/1.0.0
- Code Repository: https://github.com/OSTrails/FAIR_assessment_output_specification/
- Version: 1.0.0
- Release (in GitHub): https://github.com/OSTrails/FAIR_assessment_output_specification/releases/tag/v1.0.0
- License: CC-BY 4.0


FAIR Champion
^^^^^^^^^^^^^

FAIR Champion is a general-purpose FAIR assessment tool intended to be used by all communities and for all digital objects. In this release, FAIR Champion is aware of the 22 FAIR Tests (below), but any test, from any provider, can be registered so long as the test generates a metadata descriptor compliant with the FAIR Reference Model defined by OSTrails. The OpenAPI interface descriptor for this release is only partially complete; the Champion has a variety of functions related to new test registration and benchmark registration that are currently pending decisions by the OSTrails project.

- Persistent identifier: https://tools.ostrails.eu/champion/sets/
- Code repository: https://github.com/OSTrails/FAIR-Champion
- Version: Release v1
- Release: https://github.com/OSTrails/FAIR-Champion/releases/tag/1.0.0
- License: MIT


FAIR Champion Tests
^^^^^^^^^^^^^^^^^^^

A set of 22 tests for FAIRness. These are generic tests for all four FAIR facets – F, A, I, R – and do not represent any specific community or digital object. All tests require the GUID of the digital object’s metadata as input.  Output follows the FAIR Test Results schema (https://w3id.org/ftr/1.0.0).

- Persistent identifier: https://tests.ostrails.eu/tests
- Code repository:  https://github.com/OSTrails/FAIR-Core-Tests
- Version: Release v1
- Release:  https://github.com/OSTrails/FAIR-Core-Tests/releases/tag/1.0.0
- License: MIT


FOOPS! Test and metric catalogue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Ontology Pitfall Scanner for FAIR is a FAIR assessment tool for vocabularies and ontologies. In this release, FOOPS! has been adapted to comply with the FTR specification. A catalog of test descriptions has been made available in https://w3id.org/foops/catalogue. The release contains the source code of the tools, as well as the machine-readable and human-readable documentation of all tests, metrics and benchmarks associated with the tool.

- Persistent identifier: https://w3id.org/foops/catalogue
- Zenodo link (latest release): https://doi.org/10.5281/zenodo.14767999
- Code repository: https://github.com/oeg-upm/fair_ontologies
- Version: 0.2.0
- Release: https://github.com/oeg-upm/fair_ontologies/releases/tag/v0.2.0
- License: Apache-2.0


FAIR Data Point
^^^^^^^^^^^^^^^

The FAIR Data Point software is maintained by a third party (the “FAIRDataTeam”). In OSTrails we utilize the FAIR Data Point (FDP) in its configuration as an “index”, using the 16.x releases of the software suite in DockerHub.  FDP Index is the first implementation of a test registry and will include many of the descriptions from the FAIR Champion and FOOPS!

- Identifier: https://tools.ostrails.eu/fdp-index/
- Code repository: https://github.com/FAIRDataTeam
- Version: Docker Image version 16.x
- Release: N/A
- License: MIT


FAIR Data Point Index Proxy
^^^^^^^^^^^^^^^^^^^^^^^^^^^

An early prototype of a “proxy” service that allows native DCAT records to be registered in a FAIR Data Point Index.

- Identifier: https://tools.ostrails.eu/fdp-index-proxy
- Zenodo link (latest release)
- Code repository: https://github.com/OSTrails/FDP-Index-Proxy
- Version:  Release v1.0.0
- Release:  https://github.com/OSTrails/FDP-Index-Proxy/releases/tag/v1.0.0
- License: MIT


FAIRsharing Registry
^^^^^^^^^^^^^^^^^^^^

FAIRsharing is a registry of standards, databases, policies and FAIR assistance conceptual components. Registration of FAIR principles/dimensions, metrics, and benchmarks within FAIRsharing allows human- and machine-readable integration of the FAIR assessment components within the wider research landscape, and is key to discovery of these resources as well as for the implementation of the tests themselves via the rich metadata contained within the registry. Rather than being a specific tool release, it is the extension to FAIRsharing with the new FAIRassist registry which is relevant to the other Commons resources described in this section.

- Identifier: https://fairsharing.org/
- Code repository: https://github.com/FAIRsharing/fairsharing.github.io
- Version:  Continuous release

Cross-Cutting and Supporting Resources
--------------------------------------

*(No resources yet in this component.)*
