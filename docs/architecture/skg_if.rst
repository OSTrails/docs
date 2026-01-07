Architecture: SKG IF
====================

.. page-authors::
    Andrea Mannocci
    Paolo Manghi


This page introduces the Scientific/Scholarly Knowledge Graph Interoperability Framework (SKG-IF). It outlines its motivation, relation to key elements, and applications in OSTrails.

The `SKG-IF data model <https://skg-if.github.io/interoperability-framework>`_ is designed to enhance interoperability among different knowledge graph systems and platforms used in research. It facilitates the exchange and use of data across these systems by defining a shared language and standardised operations. Researchers or end-users are not expected to interact directly with the SKG-IF. Instead, it enables automated workflows and interoperability between services, enhancing the research ecosystem's efficiency and machine-actionability.

OSTrails SKG-IF is based on the RDA SKG interoperability framework. By providing a standardised approach to modelling a core set of scholarly data, the SKG-IF supports diverse applications involving compatible SKGs, such as combining SKGs to build new ones or exchanging data between SKGs to benefit from each other's construction methods. OSTrails will extend the existing RDA model of SKGs, propose (a mechanism for) model extensions and an API that can be used to enable scientific discovery and assessment. The OSTrails project will do so in the context of, or in close collaboration with, the RDA SKG-IF WG adding a scientific perspective to the previous scholarly one.

More specifically, SKG-IF data model entities are currently described with a comprehensive set of metadata properties, initially agreed on by the existing SKG community of stakeholders (DataCite, OpenCitation, Crossref, OpenAlex, OpenAIRE Graph), inspired also by existing metadata standards or best practices such as EuroCRIS/CERIF and now the perspective of the scientific communities. The model is agnostic of specific PID schemes or vocabularies, enabling cross-SKG interoperability by agreeing on a common structure and sharing of specific semantics. When PIDs or vocabularies are requested (e.g. resource types), properties require the vocabulary name and the specific value. Finally, the IF adopts JSON-LD, a widely recognised data exchange standard, to ensure seamless data exchange and semantic interoperability.

The work on SKG-IF is performed in the context of RDA, guaranteeing a broad set of stakeholders taking part in the decision making. OSTrails brings to the Working Group the requirements arising by scientific communities and service providers in achieving the project objectives. The project roadmap may, therefore, potentially not always be synced and aligned with the RDA WG’s. To this aim, as described below, in its first year OSTrails has co-designed and strongly contributed to the definition of SKG-IF extensions. Extensions are a mechanism allowing a community to define “customizations” of the SKG-IF core model, such as new entities, new properties of existing entities, or new relationships. Extensions, today part of the SKG-IF framework, can compensate the difference in rhythm, when manifesting, between an RDA WG and project objectives, which are driven by deadlines and deliverables. Starting from interoperability use-cases identified in the project, OSTrails partners have identified (i) which entities of the SKG data model can be adopted to meet their requirements and, when such entities are missing, (ii) the SKG extensions required to fulfil them.

For more information please refer to: Miksa, T., Wilkinson, M., Manghi, P., & Suchánek, M. (2025). **D1.4 OSTrails Interoperability Reference Architecture V1**. Zenodo. https://doi.org/10.5281/zenodo.14795000
