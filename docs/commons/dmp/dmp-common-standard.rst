RDA DMP Common Standard for maDMPs
==================================

.. page-authors::
    Tomasz Miksa
    Marek Suchánek


The **RDA DMP Common Standard for machine-actionable Data Management Plans (maDMPs)** defines a minimal, interoperable data model for representing information contained in Data Management Plans in a machine-actionable way.

The standard provides a shared vocabulary and structure for core DMP concepts that are common across domains, funders, and infrastructures. It is designed to enable consistent interpretation and exchange of DMP information between systems, while remaining independent of specific implementations, workflows, or regional policies.

Version and usage
-----------------

The DMP Commons currently build on **version 1.2** of the RDA DMP Common Standard:

- https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/tree/v1.2

This version serves as the **foundational layer** for the DMP Commons and is used as the base model for higher-level specifications: :doc:`OSTrails Application Profile <application-profile>` and then :doc:`API specification <madmp-api-specification>`. All extensions and constraints introduced by the DMP Commons are defined as additions on top of this common core, ensuring compatibility with the RDA standard.

Scope and role within the DMP Commons
-------------------------------------

Within the DMP Commons, the RDA DMP Common Standard:

- Defines the **minimum set of concepts** needed to describe a DMP in a machine-actionable way
- Establishes a **shared semantic baseline** across tools and services
- Enables interoperability without constraining internal data models or system architectures

The standard intentionally avoids domain-specific requirements or policy-driven constraints. Such specializations are addressed at higher layers (e.g. application profiles), allowing the common standard to remain stable and broadly applicable.

.. figure:: https://raw.githubusercontent.com/RDA-DMP-Common/RDA-DMP-Common-Standard/refs/tags/v1.2/docs/diagrams/maDMP-diagram.png
    :alt: RDA DMP Common Standard for maDMPs v1.2
    :target: https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/tree/v1.2

    RDA DMP Common Standard for maDMPs v1.2

Community governance and maintenance
------------------------------------

The RDA DMP Common Standard is developed and maintained by the community under the Research Data Alliance (RDA). Issues, discussions, and proposals related **directly to the standard itself** are handled within its established community processes.

Relevant resources include:

    - **Specification repository**: https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard
    - **Issue tracker and discussions**: https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/issues
    - **RDA Working Group page**: https://www.rd-alliance.org/groups/dmp-common-standards-wg

These channels are the authoritative venues for proposing changes, reporting issues, and discussing the evolution of the standard.

Contribution and future evolution
----------------------------------

In OSTrails and DMP Commons, we actively **collaborate with and contribute to the evolution of the RDA DMP Common Standard**.

This collaboration is driven by practical experience gained through building the :doc:`OSTrails Application Profile <application-profile>` and also API on top of the standard, as well as by identifying gaps or ambiguities that affect interoperability beyond specific infrastructures or regional contexts.

Proposed improvements are intentionally **not limited to OSTrails, EOSC, or Europe-specific needs**, but aim to strengthen the standard for the broader international community and future versions of the specification.

As the RDA DMP Common Standard evolves, the DMP Commons will track and align with new versions, ensuring continuity while supporting incremental adoption.

References
----------

.. bibliography::
    :list: bullet
    :filter: False
    :keyprefix: dmp-common-standard-
    :labelprefix: dmp-common-standard-

    Miksa_RDA_DMP_Common
