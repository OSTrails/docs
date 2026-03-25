OSTrails Application Profile for maDMPs
=======================================

.. page-authors::
    Tomasz Miksa
    Marek Suchánek
    Jana Martínková


The **OSTrails Application Profile (AP) for machine-actionable Data Management Plans (maDMPs)** is a tailored extension of the :doc:`RDA DMP Common Standard (DCS) for maDMPs <dmp-common-standard>`.

It is designed to enhance interoperability while addressing requirements from national and thematic pilots, often reflecting specific funder and community templates. The profile provides a list of additional terms that can be used to express information contained in DMPs in a machine-actionable way.

Upon successful review, some of the fields from the AP will be incorporated into the RDA DCS. This process is still ongoing and requires broader community consensus and RDA involvement.

The consolidated list of fields and their definitions is available in the :ref:`OSTrails AP Extension <ostrails-ap-extension>` section.

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

.. _ostrails-ap-extension:

RDA DMP Common Standard for maDMP Extension
-------------------------------------------

Based on the various consolidated inputs for OSTrails pilots, DMP platform owners and operators, and other stakeholders, we designed the following fields as needed extensions to the `RDA DMP Common Standard for maDMPs <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard>`_. The table below lists the fields, their types, cardinality, and descriptions. This list is not final and may evolve as the application profile matures and as further requirements are consolidated:

.. list-table::
   :header-rows: 1
   :class: small-table

   * - Entity
     - Field
     - Type
     - Cardinality
     - Description
   * - `DMP <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#dmp_table>`_
     - ``version``
     - ``string``
     - ``0..1``
     - Version tag of the DMP, marking its iteration or update status. It can be used in addition to existing timestamp fields to provide a more human-readable versioning scheme, especially in cases where DMPs undergo multiple revisions.
   * - `DMP <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#dmp_table>`_
     - ``license``
     - `License <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#license_table>`_ (nested)
     - ``0..1``
     - The license under which the DMP itself is published. This field allows for specifying the terms of use and sharing for the DMP document, which can be important for transparency and reuse.
   * - `DMP <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#dmp_table>`_
     - ``rights``
     - ``string``
     - ``0..1``
     - A general field to capture any rights information related to the DMP that may not be covered by the license field. This could include specific access restrictions, embargoes, or other conditions that apply to the DMP or its content.
   * - `DMP <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#dmp_table>`_
     - ``data_access``
     - ``open``, ``closed``, ``shared``
     - ``0..1``
     - A field to indicate the intended access level for the data described in the DMP. This can help clarify whether the data will be openly available, restricted to certain users, or shared under specific conditions.
   * - `Project <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#project_table>`_
     - ``acronym``
     - ``string``
     - ``0..1``
     - A short, memorable identifier for the project associated with the DMP (if applicable). This can facilitate easier reference and communication about the project, especially in contexts where the full project title may be lengthy or complex.
   * - `Dataset <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#dataset_table>`_
     - ``documentation``
     - ``string``
     - ``0..1``
     - Comments about documentation for the dataset, including any relevant details about its creation, processing, or usage.
   * - `Dataset <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#dataset_table>`_
     - ``methodology``
     - ``string``
     - ``0..1``
     - A description of the methods used to collect, process, or analyze the data in the dataset.
   * - `Dataset <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#dataset_table>`_
     - ``target_audience``
     - ``string``
     - ``0..1``
     - Information about the intended audience for the dataset, which can help clarify who the data is meant for and how it should be used.
   * - `Dataset <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#dataset_table>`_
     - ``naming_convention``
     - ``string``
     - ``0..1``
     - A description of an approach to naming datasets, which can improve discoverability and consistency across different platforms or repositories.
   * - `Distribution <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#distribution_table>`_
     - ``conforms_to``
     - ``string``
     - ``0..*``
     - A list of standards, formats, or specifications that the distribution adheres to, which can help clarify its interoperability and compatibility with various tools and platforms.
   * - `Distribution <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#distribution_table>`_
     - ``format_justification``
     - ``string``
     - ``0..1``
     - Justification for the chosen format of the distribution (i.e. why a specific format was selected for the data distribution), which can provide insights into considerations around usability, accessibility, or technical constraints.
   * - `Distribution <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#distribution_table>`_
     - ``restriction_explanation``
     - ``string``
     - ``0..1``
     - Explanation for any restrictions placed on the distribution, which can help clarify the conditions under which the data can be accessed or used.
   * - `Distribution <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#distribution_table>`_
     - ``access_methods``
     - ``string``
     - ``0..1``
     - A description of the methods used to access the distribution, which can help clarify the steps required to obtain and use the data.
   * - `Cost <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#cost_table>`_
     - ``unit``
     - ``string``
     - ``0..1``
     - Unit of the cost (e.g., PM, MHR, EUR), which can help clarify the basis for the cost calculation and facilitate comparisons across different DMPs or projects.
   * - `Cost <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard?tab=readme-ov-file#cost_table>`_
     - ``type``
     - ``string``
     - ``0..1``
     - Type of the cost (e.g., personnel, storage, processing), which can help clarify the nature of the cost and its relevance to different aspects of data management.
