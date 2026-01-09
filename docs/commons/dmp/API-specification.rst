OSTrails maDMP API Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. page-authors::
    Tomasz Miksa


Overview
--------

The **maDMP API** is a standardized interface designed to enable seamless exchange of information between machine-actionable Data Management Plans (maDMPs) and other research data management (RDM) services. It is developed jointly with the Research Data Alliance maDMP API Working Group.

The API specification is published as an OpenAPI document, ensuring interoperability and ease of integration across diverse platforms.

Objectives
----------

The main objectives of the maDMP API are:

* **Promote reuse of information from DMPs**
  Facilitate the transfer of information to and from DMPs to inform and automate actions within other research software systems.

* **Enable interoperability and interchangeability of DMP platforms**
  Ensure that any DMP tool can be integrated into diverse contexts without compatibility concerns.

* **Reduce reliance on static text documents**
  Move away from narrative PDF-based DMPs toward actionable, API-driven solutions using persistent identifiers.

* **Enhance the quality and timeliness of DMPs**
  Improve accuracy by sourcing data directly from systems where RDM activities occur.

Involved Tools
--------------

The development and adoption of the maDMP API involve collaboration with several DMP platforms and services, including:

* Argos
* DAMAP
* DMPonline
* DMP OPIDoR
* DMP Tool
* DSW
* DataPLAN

These tools will implement the API endpoints to enable interoperability and integration with other services such as data repositories, FAIR assessment tools, and virtual research environments.

External Resources
------------------

* The API is developed jointly with the `Research Data Alliance maDMP API working group <https://www.rd-alliance.org/groups/common-application-programming-interface-api-for-machine-actionable-data-management-plans-madmps/activity>`_.

* The charter of the group can be found at the `RDA maDMP API WG page <https://www.rd-alliance.org/groups/common-application-programming-interface-api-for-machine-actionable-data-management-plans-madmps/work-statement>`_.

* The API specification is in this GitHub repository: `RDA-DMP-Common/common-madmp-api <https://github.com/RDA-DMP-Common/common-madmp-api>`_.

* The OpenAPI documentation can be accessed directly at: `rda-dmp-common.github.io/common-madmp-api <https://rda-dmp-common.github.io/common-madmp-api/>`_.

Work in Progress
----------------

The API is under active development. The current specification reflects the consensus of the working group and is being tested by participating tools. Future updates will incorporate feedback from the community and ensure broad compatibility.
