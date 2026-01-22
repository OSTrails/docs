OSTrails Metadata Model for SKGs
==================================

The RDA Scholarly Knowledge Graph Interoperability Framework (SKG-IF) Core Data Model defines a minimal, interoperable metadata model for representing SKG data in a machine-actionable way.

The model is used to describe the main SKG-IF entities, their attributes, and their relations, using Semantic Web technologies. It reuses and aligns existing ontologies that address specific scholarly communication scenarios, ensuring compatibility with the overall aims of SKG-IF while avoiding reinvention of established models.

The SKG-IF Core Data Model, summarised in Graffoo diagrams, supports the representation of the following key entities:

- **Agent**: individuals or organisations (or other acting entities) involved in the creation, publication, dissemination, curation, or assessment of research products.
- **Data source**: services or platforms where research products (metadata and, where applicable, files) are stored, preserved, made discoverable, and accessed.
- **Grant**: funding awarded by a funding body to one or more agents.
- **Research product**: research outputs of different types, such as research literature, research data, research software, or other categories.
- **Topic**: scientific disciplines, subjects, or keywords relevant to a research product and its context.
- **Venue**: publishing or dissemination channels through which research products are made available (e.g., journals, conferences, platforms).

The SKG-IF Core Data Model is implemented as an OWL ontology, the SKG-IF Ontology (SKG-O). Rather than introducing yet another standalone bibliographic ontology, SKG-O aggregates and organises complementary ontological entities from several existing vocabularies used within SKG-IF, providing a coherent space for descriptive metadata compliant with the SKG-IF Data Model.

SKG-O is structured into six ontological modules, one for each SKG-IF entity type, all formally imported into the main ontology:

- **SKG-O**: agent – https://w3id.org/skg-if/ontology/agent/
- **SKG-O**: data-source – https://w3id.org/skg-if/ontology/data-source/
- **SKG-O**: grant – https://w3id.org/skg-if/ontology/grant/
- **SKG-O**: research-product – https://w3id.org/skg-if/ontology/research-product/
- **SKG-O**: topic – https://w3id.org/skg-if/ontology/topic/
- **SKG-O**: venue – https://w3id.org/skg-if/ontology/venue/

Version and usage
------------------
Within the SKG Commons, the SKG-IF Core Data Model and SKG-O serve as the foundational layer on which higher-level specifications are built: SKG-IF Extensions, application profiles, and the SKG Commons API specifications. All additional constraints and specialisations are defined on top of this core model, ensuring alignment with the RDA SKG-IF framework.

SKG-IF data produced under the Interoperability Framework align with SKG-O via the SKG-IF JSON-LD context, which binds JSON structures to ontology terms. Furthermore, a dedicated SHACL shapes document is provided for semantic validation of data against the Core Data Model, ensuring conformance and consistency across implementations.

Scope and role within the SKG Commons
----------------------------------------

Within the SKG Commons, the SKG-IF Core Data Model:

- Defines the minimum set of concepts required to describe SKGs in a machine-actionable, semantically rich way
- Establishes a shared semantic baseline across tools and services
- Enables interoperability without dictating internal data models or architectures in individual systems

Domain- or policy-specific requirements are intentionally handled at higher layers (e.g., SKG-IF Extensions and application profiles). This separation keeps the core model stable, reusable, and broadly applicable across communities and infrastructures.

Community governance and maintenance
---------------------------------------
The SKG-IF Core Data Model and SKG-O are developed and maintained by the community within the Research Data Alliance (RDA) SKG-IF activities. Issues, discussions, and change proposals concerning the model and ontology are managed via the established RDA community processes.

Typical resources include:

    * `SKG-IF Framework: <https://skg-if.github.io/interoperability-framework/>`_
    * `SKG-IF on GitHub: <https://github.com/skg-if>`_
    * `JSON-LD Context: <https://skg-if.github.io/context/>`_

These venues are the authoritative channels for proposing changes, reporting issues, and discussing the ongoing evolution of the SKG-IF Core Data Model and its ontology.

