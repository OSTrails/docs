Architecture: DMP IF
====================

.. page-authors::
    Tomasz Miksa

An **interoperability framework** refers to a set of guidelines, standards, and protocols that ensure the ability of different systems, applications, or organizations to work together effectively, exchanging data and functions seamlessly despite differences in their underlying technologies. The framework typically addresses the technical, semantic, and organizational aspects needed to facilitate collaboration and integration between disparate systems.

The **DMP-IF** consists of:
    * RDA DMP **common standard** for machine-actionable DMPs (DCS),
    * OSTrails **application profile** for maDMPs,
    * maDMP Application Programming Interface (**API**).

The DMP-IF follows this definition and is designed with DMP Platforms in mind but can be used by any service or tool that exchanges maDMPs. The IF does not prescribe internal organisation of services, e.g. their architecture or how they represent information internally. The IF focuses on how the information is exchanged with other services, i.e. defines concepts and models to represent the information, as well as actions that can be performed to get or modify information in a service implementing the DMP-IF. For example, listing all datasets described by a DMP, including their identifiers and licences, is performed in a unified way, independent of the underlying implementation. The DMP-IF addresses the technical and semantic layers only.

The **common standard** is an RDA recommendation. It defines a minimum set of concepts used to model information in DMPs common for most use cases. The **application profile** builds on top of the common standard. It provides additional concepts and constraints necessary to support the interactions identified in the pathways and reference architecture. Thus, it provides more concepts and more constraints that reflect the needs of OSTrails as whole and eventually EOSC. While both focus on establishing a common language on how information contained in DMPs is expressed in a machine-actionable way, the API provides a set of methods that can be used to perform specific actions on DMPs. The structure of messages exchanged with the use of the API is based on the common language defined by the common standard and the application profile.

The DMP-IF is **relevant to software engineers and service operators** who want to standardise how information on DMPs is exchanged. End-users, i.e. researchers, are not supposed to be aware of the DMP-IF. The DMP-IF facilitates the reuse and exchange of information so that typical RDM tasks can be automated, and DMPs are a place where all the information relevant to data management, e.g. type of data, storage location, access permissions, etc., are kept. DMP platforms should thus become a source of up-to-date information for other services that depend on them, e.g. researchers involved in a project described by a DMP should automatically get access to relevant equipment and repositories described by the DMP. As a result, creating the DMP should primarily benefit researchers by facilitating data management of their typical tasks and become less a one-time exercise to meet formal requirements.

**Adopting the DMP-IF** can be performed gradually and tailored to the needs of the specific use case. Yet, full interoperability can only be achieved when the specific service implements the complete maDMP API. This is because the API reflects the community agreement on the common language used to describe the DMP contents and makes technical decisions that leave less room for interpretation, e.g. choice of communication protocol, such as HTTP, and ways to serialise the exchanged messages, for instance, using JSON.

Ongoing and future work
***********************

Together with the RDA DMP Common Standards WG we perform the maintenance of the recommendation. The RDA DMP Common Standards working group will be able to accept only minor and small changes to the recommendation. These will be mostly refinements bringing clarity or changes that are backward-compatible. As a result, we will have a stable and up-to-date set of concepts shared across the whole DMP community. Any major changes that could considerably influence the design of the recommendation need to be performed by a new working group – this is an RDA requirement. For this reason, OSTrails develops the OSTrails application profile to incorporate bigger changes that also cover the project-specific needs, which may not be shared across the whole RDA community.

By defining one application profile, we want to mitigate a situation when every use case owner defines their own set of extensions. For example, we will define a set of concepts that support the requirements of most funders instead of having extensions per funder. This should prevent situations in which overlapping concepts are represented differently, and hence, the interoperability is lower.  While the DCS is an official recommendation of RDA and must leave many decisions open, e.g., which type of controlled vocabulary to use for identifier types, the OSTrails application profile imposes additional constraints on the RDA recommendation that are relevant within the OSTrails and EOSC contexts. For example, the application profile may have stricter requirements regarding the use of persistent identifiers (rather than URLs) or may require the use of specific controlled vocabularies.

The broader objectives of the maDMP API are as follows:
    * Enable interoperability and interchangeability of DMP platforms: Ensure that any DMP tool can be utilised in diverse contexts without compatibility concerns.
    * Reduce reliance on static text documents: Shift away from narrative DMP formats, such as PDFs, towards enhanced use of persistent identifiers where appropriate.
    * Promote the reuse of information from DMPs: Facilitate the transfer of information from DMPs to inform and drive actions within other RDM systems.
    * Enhance the quality and timeliness of DMPs: Improve accuracy by sourcing data directly from systems where RDM activities are conducted.

This approach aims to establish a robust framework for seamless integration and automation in the RDM ecosystem, significantly advancing the utility and efficiency of DMPs. The maDMP API does not replace existing APIs offered by DMP Platforms. There are still operations that are specific to each platform. The maDMP API standardises typical interactions with maDMPs in a similar fashion as the DCS, which represents consensus on most common DMP elements in most settings, but not all of them.
