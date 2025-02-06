Architecture: FAIR IF
=====================


FAIR Test Results specification and SHACL shapes:  
******
FTR is the first OWL implementation of the FAIR Reference model described in Deliverables D1.2 and D.1.4. The reference model extends W3C standards such as [DCAT](https://www.w3.org/TR/vocab-dcat-3/), [DQV](https://www.w3.org/TR/vocab-dqv/) and [PROV](https://www.w3.org/TR/prov-o/) to describe test results, test definitions, metrics, benchmarks and their interpretation to generate a FAIR assessment score. 

The code release includes the vocabularies, definitions, specifications in machine-readable format and a set of SHACL validation rules to ensure tests and metrics are defined according to the specification. 

- Persistent identifier: https://w3id.org/ftr/1.0.0 
- Code Repository: https://github.com/OSTrails/FAIR_assessment_output_specification/ 
- Version: 1.0.0 
- Release (in GitHub): https://github.com/OSTrails/FAIR_assessment_output_specification/releases/tag/v1.0.0 


FAIR Champion 
******
FAIR Champion is a general-purpose FAIR assessment tool intended to be used by all communities and for all digital objects. In this release, FAIR Champion is aware of the 22 FAIR Tests (below), but any test, from any provider, can be registered so long as the test generates a metadata descriptor compliant with the FAIR Reference Model defined by OSTrails. The OpenAPI interface descriptor for this release is only partially complete; the Champion has a variety of functions related to new test registration and benchmark registration that are currently pending decisions by the OSTrails project. 

- Persistent identifier: https://tools.ostrails.eu/champion/sets/  
- Code repository: https://github.com/OSTrails/FAIR-Champion 
- Version: Release v1 
- Release: https://github.com/OSTrails/FAIR-Champion/releases/tag/1.0.0 


FAIR Champion Tests
****** 
A set of 22 tests for FAIRness.  These are generic tests for all four FAIR facets – F, A, I, R – and do not represent any specific community or digital object. All tests require the GUID of the digital object’s metadata as input.  Output follows the FAIR Test Results schema (https://w3id.org/ftr/1.0.0) 

- Persistent identifier: https://tests.ostrails.eu/tests 
- Code repository:  https://github.com/OSTrails/FAIR-Core-Tests 
- Version: Release v1 
- Release:  https://github.com/OSTrails/FAIR-Core-Tests/releases/tag/1.0.0 
 

FOOPS! Test and metric catalogue
****** 
The Ontology Pitfall Scanner for FAIR is a FAIR assessment tool for vocabularies and ontologies. In this release, FOOPS! has been adapted to comply with the FTR specification. A catalog of test descriptions has been made available in https://w3id.org/foops/catalogue. The release contains the source code of the tools, as well as the machine-readable and human-readable documentation of all tests, metrics and benchmarks associated with the tool. 

- Persistent identifier: https://w3id.org/foops/catalogue 
- Zenodo link (latest release): https://doi.org/10.5281/zenodo.14767999  
- Code repository: https://github.com/oeg-upm/fair_ontologies 
- Version: 0.2.0 
- Release: https://github.com/oeg-upm/fair_ontologies/releases/tag/v0.2.0  


FAIR Data Point:
****** 
The FAIR Data Point software is maintained by a third party (the “FAIRDataTeam”). In OSTrails we utilize the FAIR Data Point (FDP) in its configuration as an “index”, using the 16.x releases of the software suite in DockerHub.  FDP Index is the first implementation of a test registry and will include many of the descriptions from the FAIR Champion and FOOPS!  

- Identifier: https://tools.ostrails.eu/fdp-index/ 
- Code repository: https://github.com/FAIRDataTeam 
- Version: Docker Image version 16.x 
- Release: N/A 
     

FAIR Data Point Index Proxy:
****** 
An early prototype of a “proxy” service that allows native DCAT records to be registered in a FAIR Data Point Index.

- Identifier: https://tools.ostrails.eu/fdp-index-proxy 
- Zenodo link (latest release) 
- Code repository: https://github.com/OSTrails/FDP-Index-Proxy 
- Version:  Release v1.0.0 
- Release:  https://github.com/OSTrails/FDP-Index-Proxy/releases/tag/v1.0.0 

  