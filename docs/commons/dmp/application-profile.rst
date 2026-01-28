OSTrails Application Profile for maDMPs
=======================================

.. page-authors::
    Tomasz Miksa
    Marek Suchánek
    Jana Martínková


The **OSTrails Application Profile (AP) for machine-actionable Data Management Plans (maDMPs)** is a tailored extension of the :doc:`RDA DMP Common Standard (DCS) for maDMPs <dmp-common-standard>`.

It is designed to enhance interoperability while addressing requirements from national and thematic pilots, often reflecting specific funder and community templates. The profile provides a list of additional terms that can be used to express information contained in DMPs in a machine-actionable way.

Upon successful review, some of the fields from the AP will be incorporated into the RDA DCS. This process is still ongoing and requires broader community consensus and RDA involvement.

The work presented on this page reflects the **working draft as of January 2026**.

Purpose and scope
-----------------

The OSTrails AP enhances interoperability by introducing **additional entities, fields, constraints, and usage patterns** that are not covered by the minimal core defined in the DMP Common Standard.

It is designed to:

- Support **information requirements imposed by funding agencies**
- Reflect **national, institutional, and thematic practices** around DMPs
- Enable reliable machine-to-machine interactions in the European research data management ecosystem

Technically, the application profile is specified in accordance with the extension mechanisms foreseen by the DMP Common Standard and forms a core artefact of the DMP Commons as a formal description of the maDMP data structure.

Iterative and community-driven development
------------------------------------------

The OSTrails Application Profile is developed **iteratively**.

Rather than defining a fixed, one-time specification, the profile continuously evolves by consolidating requirements gathered from multiple perspectives and real-world implementations. This approach allows the AP to respond to emerging needs while maintaining internal consistency and interoperability.

The application profile is intentionally designed as an artefact that is **by-design ready for future evolution**, both within the OSTrails project and beyond it.

At present, the OSTrails AP is in an **early stage of development**, and its structure and content are expected to mature through successive iterations.

Sources of requirements and inputs
----------------------------------

The OSTrails Application Profile is informed by a wide range of inputs, including:

- **Funding agency DMP templates** and policy requirements
- **European and EOSC-level guidelines** and interoperability recommendations
- **National and regional DMP practices** identified through pilots
- **Institutional requirements**, including those of research-performing   and research-supporting organisations
- **Thematic and domain-specific guidelines** from research communities
- **Feedback from national and thematic pilots within OSTrails**
- **Practical implementation experience** from DMP platforms and services
- **Gaps and ambiguities identified in the DMP Common Standard** when applied in operational settings

These inputs are analysed, consolidated, and progressively incorporated into the application profile. Some of the exemplary efforts are documented in the :doc:`maDMP mappings <mappings/index>`.

Relationship to the DMP Common Standard
---------------------------------------

The OSTrails Application Profile is a **formal extension** of the :doc:`RDA DMP Common Standard (DCS) for maDMPs <dmp-common-standard>`.

This means that the profile may introduce:

- new entities,
- additional fields or attributes,
- more specific constraints on existing elements,
- clarified usage patterns for machine-actionable exchange.

At the same time, **compatibility is a core design principle**. Every maDMP that conforms to the OSTrails Application Profile is also compliant with the broader and in a sense simpler DMP Common Standard.

This ensures that DMPs expressed using the OSTrails AP remain interoperable with services that only support the core RDA model, while enabling richer interactions where the application profile is implemented.
