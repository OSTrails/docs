.. _tool-registries:

Registries
==========

In addition to testing and assessment tools, the OSTrails project has also developed a number of
other tools that support the testing ecosystem, including registries of FAIR assessment
components and software tools.

.. contents:: On this page
    :local:
    :depth: 2

.. _fairsharing-registry:

FAIRsharing Registry
----------------------

Across all disciplines, there are thousands of repositories (databases and knowledge bases), as well as
community-developed standards for the identification, citation, and reporting of digital objects (DOs),
such as datasets, software, and research materials. Making the right choice is challenging, but understanding
this evolving landscape is essential: standards and repositories are fundamental pillars of the FAIR
Principles.

`FAIRsharing <https://fairsharing.org/>`_ is a curated, informative, and educational
resource on data and metadata standards, inter-related to databases and data policies across all disciplines.
It guides:

- **Consumers**, to discover, select, and use standards and repositories with confidence;
- **Producers**, to make their resources more discoverable, widely adopted, and cited; and
- **Third-party tools**, by providing trustworthy content to promote standards and databases.

FAIRsharing is a core integration component within a variety of research data management tools, including
technical solutions for FAIR assessment and evaluation as well as data management plan (DMP) creation. It is
recommended within infrastructures such as **EOSC** and **ELIXIR**, as well as by research data management
communities including the **Research Data Alliance (RDA)**.

FAIRsharing provides more than **40 richly described metadata fields and relationships**, including:

- How standards are related to each other (e.g. which terminologies are required by discipline-specific formats),
- Which repositories implement specific standards,
- The maturity status of standards and databases,
- Which data policies recommend them, and
- Which digital object (DO) types and disciplines are in scope.

All FAIRsharing information is available in a **machine-actionable format**, using DCAT and JSON, and can be
accessed via content negotiation and FAIRsharing APIs to support advanced queries.

Community Engagement and Curation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FAIRsharing has a strong user community and an ongoing `Community Champion Programme
<https://fairsharing.org/community_champions>`_. This programme
brings together domain and discipline experts who:

- Act as advocates for standards, databases, and policies for digital objects,
- Create educational material to support discovery, use, and adoption of these resources, and
- Enrich FAIRsharing content by improving the description and discoverability of standards, repositories, and policies.

OSTrails Cluster representatives participate as Champions and collaborators, working with the programme to
advance open and FAIR data management within the project.

FAIRsharing and the Assess-IF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Assess-IF requires high-quality information on standards and digital object types. OSTrails Cluster
representatives therefore engage with FAIRsharing to:

- **Curate FAIRsharing content**, ensuring that domain-agnostic and discipline-specific standards and data resources are represented according to Cluster usage, recommendations, and community best practices. This curation enables these resources to be used within FAIR assistance and evaluation workflows.
- **Curate FAIRassist content**, by registering and maintaining FAIR assistance benchmarks and associated components. These records are essential for the development of FAIR test workflows for OSTrails Clusters, as well as thematic and national pilots.
- **Create collections of resources**, which group standards and data resources to facilitate discovery and use by humans and machines. Collections are based on community best practices and are required to support each Cluster's assessment process.

Collections also provide graphical representations of Cluster requirements, illustrating relationships
among standards and repositories (for example, which terminologies are required by specific formats, or which
identifier schemes are used by a given repository). This approach fosters reuse of common standards and
repositories across Clusters, disciplines, and communities where appropriate.

.. _fairassist-registry:

FAIRassist Registry
~~~~~~~~~~~~~~~~~~~~

The `FAIRassist registry <https://fairassist.org/registry>`_, powered by
FAIRsharing, stores records with persistent identifiers (DOIs) relating to the **conceptual components of FAIR
assistance and evaluation**.

FAIRassist and the FDP Index are complementary exemplar services that showcase:

- Registration and sharing of the components of the Assess-IF,
- Assistance with their discoverability (based on digital object types, discipline specificity, or generic scope), and
- Delivery of information and documentation to guide and support the FAIR assessment process.

In particular, FAIRassist complements the FDP registry of **software components** from the Assess-IF (tests and
algorithms) by registering the **conceptual components**, including:

- FAIR Dimensions and Principles,
- Metrics, and
- Benchmarks,

as well as their relationships and links to individual tests.

Registration with FAIRassist and FDP is strongly recommended for transparency and FAIRness. This approach
supports ease of adoption while providing clear guidance on the formality and consistency expected within an
Interoperability Framework. Through content negotiation and FAIRsharing APIs, FAIRassist provides a rich set of
human-curated data to FAIR assessments in a machine-actionable DCAT/JSON format.

Cross-linking and Ecosystem Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The cross-linking between FAIRsharing and FAIRassist enables the Assess-IF by connecting metrics and benchmarks
to the FAIRsharing graph of information, including:

- The digital objects (e.g. datasets, terminologies) applicable to a given metric or benchmark,
- The expert communities or domains for which the metric or benchmark is relevant,
- The standards or policies involved in the FAIR evaluation, and
- The assessment tools or platforms that run the evaluations.

Other tools within the OSTrails ecosystem that integrate with FAIRassist include:

- **OSTrails Wizard** – creation of Assess-IF components,
- **FAIR Champion** – running benchmarks and registering software components,
- **FOOPS!** – creation of Assess-IF components for terminologies,
- **DSW**, **damap**, and **Argos** – tools for DMP creation and evaluation.

.. _software-registry:

OSTrails Software Tools Index
--------------------------------

The OSTrails Software Tools Index provides a curated list of software tools that support the creation,
registration, and evaluation of FAIR digital objects.

It is a machine-readable index intended primarily for software agents rather than direct human browsing.
Other tools, such as the Component Authoring Tool, speak directly to the index to retrieve information about
the available tests or algorithms, or to write new information about newly created tests or algorithms. The
FAIR Validator uses the index to retrieve information about the available tests and their associated metrics
and benchmarks, and the Champion uses it to look up and provide access to both Tests and Benchmark Scoring
Algorithms. Human-readable views of this content are instead provided by platforms and registries such as
FAIR Champion and FAIRsharing.

.. raw:: html

    The homepage of the OSTrails Software Tools Index is available at:
    <a href="https://w3id.org/fdp-index" target="_blank" rel="noopener">
    OSTrails Software Tools Registry</a>.
