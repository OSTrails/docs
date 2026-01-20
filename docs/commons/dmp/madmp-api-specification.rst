maDMP API Specification
=======================

.. page-authors::
    Tomasz Miksa
    Marek Suchánek
    Vojtěch Knaisl


The **maDMP API specification** defines a common way to **programmatically interact with machine-actionable Data Management Plans (maDMPs)** across DMP platforms and related services.

The API enables uniform access to DMP information and actions, even when individual platforms differ in their internal architectures, functional focus, user experience, or integrations with other systems.

Purpose and design principles
-----------------------------

The maDMP API is designed to:

- Enable **standardised operations** over DMPs across platforms
- Support **machine-to-machine interoperability** in heterogeneous environments
- Decouple external interactions from internal system design
- Facilitate automation of research data management workflows

The API focuses on *how* DMP information is accessed and manipulated, not on *how* services internally store or manage that information. This allows platforms to evolve independently while exposing a predictable and interoperable interface.

Relationship to the data models
-------------------------------

The maDMP API builds directly on top of the :doc:`RDA DMP Common Standard <dmp-common-standard>` and uses its concepts and structures as the semantic foundation for all exchanged messages.

The API is designed to be **flexible with respect to compatible extensions**, such as the :doc:`OSTrails Application Profile <application-profile>`. This means that:

- The API can operate over DMPs expressed using the core DMP Common Standard.
- It can also be used with extended profiles, as long as they remain compatible with the common model.

This approach allows the same API to be reused across different contexts and extensions, while preserving interoperability at the core level.

Uniform operations across DMP platforms
---------------------------------------

By implementing the maDMP API, DMP platforms expose a common set of operations that can be used consistently across systems, for example:

- searching or filtering DMPs based on various criteria,
- retrieving DMPs and their metadata,
- updating or enriching DMP information,
- creating new DMPs,
- deleting or archiving DMPs.

These operations are performed in a unified way, independent of the platform’s specific focus, user interface, or internal integrations.

Community governance and maintenance
------------------------------------

The maDMP API specification is being **developed jointly** within the `RDA Common Application Programming Interface (API) for machine-actionable Data Management Plans (maDMPs) Working Group <https://www.rd-alliance.org/groups/common-application-programming-interface-api-for-machine-actionable-data-management-plans-madmps/activity/>`_.

The working group was established during the OSTrails project and brings together experts from multiple initiatives and infrastructures to define a broadly applicable, community-endorsed API.

Relevant resources include:

    - **Specification repository**: https://github.com/RDA-DMP-Common/common-madmp-api
    - **Issue tracker and discussions**: https://github.com/RDA-DMP-Common/common-madmp-api/issues
    - **RDA Working Group page**: https://www.rd-alliance.org/groups/common-application-programming-interface-api-for-machine-actionable-data-management-plans-madmps

Documentation and versioning
----------------------------

The API is documented using OpenAPI, with rendered documentation available at:

- **OpenAPI documentation**:
  https://rda-dmp-common.github.io/common-madmp-api/

Currently, the API specification is at **version 0.1.0**, representing an early stage of development. Future versions will evolve based on community feedback, implementation experience, and emerging needs. The current specification reflects the consensus of the working group and is being tested by participating tools. Future updates will incorporate feedback from the community and ensure broad compatibility.

Involved tools
--------------

The development and adoption of the maDMP API involve collaboration with several DMP platforms and services, including:

* Argos
* DAMAP
* DMPonline
* DMP OPIDoR
* DMP Tool
* Data Stewardship Wizard (DSW)
* DataPLAN
* FAIR Wizard
* OpenCDMP

These tools will implement the API endpoints to enable interoperability and integration with other services such as data repositories, FAIR assessment tools, and virtual research environments.
