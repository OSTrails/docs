OpenAIRE Graph API
===================

The OpenAIRE Graph (http://graph.openaire.eu) is a scholarly knowledge graph designed to provide a comprehensive view of scholarly communication and research outputs at the global level. It integrates data from various sources, including publications, research datasets, projects, and authors, creating a cohesive representation of scholarly information.

Data Model
-----------

The OpenAIRE Graph employs a comprehensive data model that encapsulates a diverse range of entities essential to scholarly communication. Key entities include:

- Publications: Scholarly articles, conference papers, and other forms of research outputs.
- Research Data: Datasets: Research data associated with various scholarly works.
- Research Software: Tools and applications developed for research purposes.
- Authors: Individual researchers and their institutional affiliations.
- Funders and Projects: Funded research initiatives and their resultant outputs.
- Organizations: Institutions, companies, funding bodies, controbuting to research and its developments.

The graph not only represents these entities but also illustrates the relationships between them. This interconnectedness allows users to explore citations, collaborations, project affiliations, and software dependencies among a vast network of research products.

.. figure:: openaire-graph.png
    :alt: SKG OpenAIRE Graph
    :align: center

    SKG OpenAIRE Graph


Content
--------

The OpenAIRE Graph populates its content by harvesting from more than 2000 trusted data sources native to scholarly communication, including:

- Crossref and DOAJ: For scholarly publishers metadata and citations.
- DataCite: For research data, software, publication metadata and citations.
- OpenCitations: For citation data.
- ORCID: Linking researchers to their work and contributions.
- Institutional repositories and CRIS systems worldwide: For research data, software, publication metadata and citations.
- ROR (Research Organization Registry): Standardizing organization identifiers and author-organization-research product affiliations.
- ArXiv, PubMed, DBLP, REPEC, and others: Covering scientific papers in specific disciplines.
- Additionally, it includes hundreds of data and software repositories sourced from research infrastructures, science clusters, and the broader European Open Science Cloud (EOSC) domain.

Today, the Graph boasts the largest collection of research products and citations, facilitating discovery, browsing, and in-depth bibliometric analysis of how knowledge and findings are shared and built upon within the scholarly community.

To know more about how it is built and how to access the data, refer to https://graph.openaire.eu/docs/.

Implementation of the SKG-IF APIs

The OpenAIRE Graph APIs are accessible from https://graph.openaire.eu/docs/apis/home. The set of APIs is being extended with the implementation of the Scholarly Knowledge Graph Interoperability Framework (SKG-IF) APIs to further enhance the accessibility and usability of the OpenAIRE Graph.

    - **Swagger API**:https://api.openaire.eu/graph/v3/api-docs/SKG-IF%20OpenAPI%20V1
    - **Endpoints**:
        - https:....//skg-if/v1/products – Returns products matching criteria
        - https:....//skg-if/v1/products/{local identifier} – Returns the product record with the given {local identifier}
    - **Current Status**:
        - Version 1.0.0 has been released as an initial draft, with the intent to extend to other endpoints serving the remaining entities.

