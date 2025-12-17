ROHub API
================

.. page-authors::
    Raul Palma
        
ROHub (https://www.rohub.org/) is an RO-Crate management platform that provides a holistic solution for the storage, lifecycle management and preservation of scientific investigations, campaigns and operational processes via research objects. 
It makes these resources available to others, allows to publish and release them through a DOI, and allows to discover and reuse pre-existing scientific knowledge. 
ROHub implements the RO-Crate specification and uses it as the standard format for serialising and exchanging research objects. 
ROHub provides the backbone to a wealth of RO centric applications and interfaces across different scientific communities. 
It is available via a public instance, and can provided also as a dedicated/private instance (Platform as a service) or on-premises. 

Architecture overview and integrations
------------------------------------------
ROHub comprises a backend component, an IAM component, (meta-) data and resource storage components and a set of user interfaces. 
The backend exposes a comprehensive REST API, which can be used by different applications. 
The user interfaces, include a reference Web Portal and a Python library. 
The ROHub portal provides a comprehensive user interface for the management and preservation of research objects, while the Python library works on top of the ROHub backend REST API, wrapping and abstracting the REST methods in user-friendly API methods that can be used, for instance, via Jupyter Notebooks. 
Additionally, various external services are integrated or leverated in ROHub, including RO added value services as well as various EOSC services.  
These include:
•	Semantic enrichment and recommendation plus a set of extended analytic services.  The former generate structured machine-readable metadata about the content of a research object including the main concepts and phrases, the entities and their type, and topical information from domains according to the Expert.ai linguistic knowledge graph, and generate recommendations based on the discovered metadata. The latter include the challenge and solution extraction, the Question Generation service, the claim analysis service, and the novelty scoring service
•	Checklist service: provides access to the minim-based checklist evaluation of research objects, used to assess their quality for different purposes, e.g., completeness, accessibility or ready to release, and according to the needs of a particular community or application.
•	Quality monitoring service: enables the evaluation of the RO through time by capturing discrete values provided by the checklist service in different moments of its evolution. 
•	FAIROs service: measures the FAIRness of Research Objects, by calculating the FAIRness of individual aggregated resources, including the Research Object itself, and then aggregating those results to calculate the over FAIR score.
•	EGI check-in, the EOSC Identity and Access Management (IAM) service that connects federated Identity Providers (IdPs) with EOSC service providers. 
•	Zenodo. ROHub allows to release and share ro-crates via Zenodo.
•	B2share. ROHub allows to release and share ro-crates via B2Share.
•	B2drop. ROHub users have the possibility to use the default ROHub storage, or B2drop as their personal storage space where the resources uploaded to their research objects will be stored. B2drop resources are synchronized with the corresponding research objects in both ways.
•	Notebooks. ROHub users can open and load the Jupyter notebooks in the ROs automatically in EGI Notebooks directly from ROHub and execute their methods/processing in an interactive computing environment (eproducible science).
•	Replay. ROHub users can open and load automatically Jupyter notebooks and reproduce their associated computing environment with Replay, including any related input datasets, directly from the ROs in ROHub. (highest reproducible science)
•	OpenAire/EOSC Research Graph. ROHub resources, particularly ROs, Jupyter notebooks and data cubes, are harvested in the graph, and thus they are findable directly from the EOSC marketplace.
•	Argos. ROHub enables the creation of ROs from DMPs in Argos, leveraging and representing all the DMP information in machine-readable format, enabling researchers to shift their DMP into machine actionable DMPs, connected with the datasets themselves.
•	ADAM. ROHub enables the aggregation of data cubes from ADAM by reference, leveraging all the available metadata available in ADAM to describe them in the RO. ROHub users can open and load data cubes in ADAM directly from ROHub for their usage and exploration


Authentication and Authorization
------------------------------------------
The ROHub Identity and Access Management (IAM) is based on Keycloak technology. 
It allows users to authenticate to ROHub and enables the single sign-on across different various services. 
The most important feature of ROHub IAM is that is integrated with EGI check-in AAI and with Pionier.ID. 
The former allows the user to authenticate through the EGI check-in service that operates as a central hub to connect federated Identity Providers (IdPs) with EOSC service providers. 
The latter allows access to the services of the PIONIER Consortium for Polish science and automatic membership in eduGain, which connects identity federations around the world, simplifying access to content, services and resources for the global research and education community.


SKG-IF implementation
------------------------------------------
Initial implementation (under testing) of OSTrails SKG-IF to expose RO-Crates as Scientific Knowledge Graphs, focused on research products.  
This required the specification and implementation of the mapping of the RO-Crate metadata to the SKG-IF data model.  
This will allow the integration and/or harvesting of RO-Crate metadata in other SKGs that will use this API to harvest metadata, like OpenAire that plans to use such API in the future for harvesting.  
Currently, OpenAire SKG harvest metadata about RO-Crates (and other key resources) from ROHub via its OAI-PMH endpoint.   

Resources and identifiers 
--------------------------------
Portal
~~~~~~~~
- Portal: https://www.rohub.org/
- re3data.org persistent identifier: http://doi.org/10.17616/R31NJN60
- FAIRSharing identifier: https://fairsharing.org/4119
- Portal documentation: https://reliance-eosc.github.io/rohub-portal-documentation/ 
- Version 4.0.2

API
~~~~~~~~
- API: https://api.rohub.org/api/
- OpenAPI: https://api.rohub.org/api/swagger/
- Redoc: https://api.rohub.org/api/redoc/ 
- OAI-PMH endpoint:  https://api.rohub.org/api/oai2d/ 
- SPARQL endpoint: https://rohub2020-api-virtuoso-route-rohub2020.apps.paas.psnc.pl/sparql/ 
- Version: 2.1.81

Python library
~~~~~~~~~~~~~~~~
- Python library: https://reliance-eosc.github.io/ROHUB-API_documentation/html/README.html 
- API library documentation: https://reliance-eosc.github.io/ROHUB-API_documentation/html/index.html  
- API library example Jupyter Notebooks: https://github.com/RELIANCE-EOSC/sample-notebooks  
- Repository: https://github.com/oeg-upm/FAIR-Research-Object
- License: MIT

support
~~~~~~~~
- ROHub in EOSC: https://open-science-cloud.ec.europa.eu/resources/datasources/21.11166%2FBA1Ba2
- Tutorial: https://reliance-eosc.github.io/ROHUB-API_documentation/html/tutorials.html  
- Training materials: https://www.reliance-project.eu/adopters/ 
- Helpdesk: https://support.pcss.pl/servicedesk/customer/portal/27  
- support email: support@rohub.org    