SKG-IF mappings
================

Overview
---------

SKG mappings are structured specifications that translate existing scholarly metadata schemas, exchange formats, or APIs into formats compliant with the SKG Interoperability Framework (SKG-IF) Core Data Model and SKG-IF Extensions. These mappings are published as part of the SKG Commons to foster interoperability and automation across Scholarly Knowledge Graph (SKG) providers.

Purpose
-------
The main goals of SKG mappings are:

- Enable machine-actionability: Transform heterogeneous, often bespoke SKG or metadata representations into structured, interoperable formats that can be consistently processed by software systems in accordance with SKG-IF.
- Support integration with SKG-related services: Facilitate connections between SKG providers and services, including CRIS/RIS systems, repositories, PID infrastructures, and other scholarly information systems.
- Provide a shared reference: Publish mappings as part of the Commons so they can be reused, profiled, and adapted by other projects, domains, and communities.

Creation Process
------------------

The development of SKG mappings follows a collaborative workflow:

1. Select a source schema, format, or interface: Identify the metadata schema, exchange format, API, or SKG model that should be aligned with SKG-IF.
2. Review SKG-IF and existing extension profiles: Familiarise yourself with the SKG-IF Core Data Model and relevant SKG-IF Extensions or application profiles. Review existing mappings where available.
3. Draft the mapping:
    - Map entities, relationships, and fields from the source specification to SKG-IF components.
    - Define validation rules, cardinalities, and controlled vocabularies (e.g., identifiers, resource types, access categories).
    - Propose additions or revisions to SKG-IF Extensions where no suitable target element exists.
4. Test usability: Validate the mapping using representative real-world datasets or graph instances to ensure that it is practical, loss-minimising, and supports intended interoperability scenarios.
5. Publish as Commons:  The validated mapping is contributed to the SKG Commons and made available for reuse and further refinement.

Integration
-----------

Once established, SKG mappings can be implemented by SKG platforms and related services to achieve interoperability. These integrations enable automated data exchange and graph enrichment, ensuring that SKGs remain consistent, up-to-date, and interoperable across the research ecosystem. The concrete implementation work lies with the respective tool and service owners; SKG mappings provide the technical guidance they need to achieve interoperability.

Mappings
--------

Below, we list SKG mappings defined for commonly used scholarly metadata sources:


.. toctree::
   :maxdepth: 1
   :titlesonly:

   DDI SKG-IF mapping <skg-if-ddi>
   RO-Crate SKG-IF mapping <skg-if-rocrate>
   OpenAIRE Graph SKG-IF mapping <skg-if-openaire>
