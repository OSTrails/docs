SKG Commons
============

.. page-authors::
    Andrea Mannocci
    Paolo Manghi
    Renaud Duyme
    Menzo Windhouwer
    Daan Broeder


The SKG Commons provide a common, reusable,
extensible, and interoperable foundation for handling data exchange between Scholarly Knowledge Graph (SKG)
interfaces across tools and services that implement the Scholarly Knowledge Graph Interoperability Framework (SKG-IF).
They specify how SKG information is modelled, constrained, and exchanged,
while remaining neutral regarding the internal design or implementation of individual systems. The main audience for the SKG Commons consists of software developers who build services to create, manage, or consume SKGs. This includes SKG providers (e.g., OpenAIRE Graph, OpenCitations), other services that manage scholarly metadata and wish to expose interoperable interfaces (e.g., FAIRSharing, RO-Hub and thematic rich metadata repositories), and services that want to integrate with such platforms, as described in the OSTrails Architecture and Pathways.

The Commons are organised as a framework composed of a shared core data model, SKG-IF community extensions to that model,
standard APIs, and shared mappings from local platform models onto the SKG-IF:

- **RDA SKG-IF Core Data Model**: The base model that captures the key SKG entities, relationships, and constraints in a machine-actionable form.
- **SKG-IF Extensions**: Community- or domain-specific specialisations of the core model that modify or add new entities, fields, and constraints to meet particular interoperability and policy requirements.
- **SKG Commons API Specifications**: Standardised APIs for programmatic access to SKG data across platforms, built on the core model and designed to work with the defined application profiles.
- **SKG mappings**: data model mappings between SKG-IF and external vocabularies, schemas, and domain models, facilitating the creation of application profiles and the alignment of SKG information with existing standards.

These layers together ensure a consistent understanding of SKG content and predictable behaviour when services interact, regardless of how they are implemented internally. This design enables platforms to evolve independently while remaining interoperable at their interfaces.


The SKG Commons primarily target software developers, system architects, and service providers who build or run SKGs and related research information services. Researchers and other end users typically do not interact with the Commons directly; instead, they benefit indirectly through improved automation, more comprehensive linking of research outputs and actors, and enhanced reuse of SKG data across systems.
The SKG Commons follow a community-driven, evolutionary approach, meaning they are intended to adapt continuously to community input, emerging practices, and new interoperability demands. They are grounded in work carried out within the Research Data Alliance (RDA), notably the SKG Interoperability Framework and associated recommendations, and they actively feed back into these communities. The framework supports stepwise adoption while still enabling full interoperability once all components are in place.

Contribution and future evolution
----------------------------------
The SKG Commons actively collaborate with and contributes to the further development of the SKG-IF Core Data Model and SKG-O.

This contribution is informed by practical implementation experience with SKG-IF Extensions, JSON-LD contexts, SHACL validation, and the SKG Commons APIs, as well as by identifying gaps or ambiguities that hinder interoperability across infrastructures, domains, or regions.

Proposed enhancements are not limited to a particular platform or geography; they aim to strengthen SKG-IF for the broader international community and future versions of the framework. As SKG-IF evolves, the SKG Commons will track and adopt new versions, preserving continuity while enabling incremental uptake of improvements.


The following resources in this section are part of the SKG Commons component.

.. toctree::
    :caption: SKGs Resources
    :maxdepth: 1
    :titlesonly:

    OSTrails Metadata Model for SKGs <skg-if-metadata-model>
    OSTrails SKG-IF API Specification <skg-if-api-specification>
    OSTrails SKG-IF Extensions <skg-if-entity-extension>
    SKG-IF mappings <mappings/index>
