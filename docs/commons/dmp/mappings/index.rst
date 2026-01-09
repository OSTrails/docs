maDMP Mappings
==============

.. page-authors::
    Tomasz Miksa

Overview
--------

**maDMP mappings** are structured documents that translate traditional Data Management Plan (DMP) templates into a machine-actionable format based on the `RDA maDMP Common Standard (DCS) <https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard>`_ and the OSTrails Application Profile (AP). These mappings are published as part of the commons to support interoperability and automation in Research Data Management (RDM).

Purpose
-------

The main goals of maDMP mappings are:

* **Enable machine-actionability**
  Convert narrative DMP templates into structured, interoperable formats that can be processed by software systems.

* **Support integration with RDM services**
  Facilitate connections between DMP platforms and services such as CRIS systems, repositories, and PID infrastructures.

* **Provide a shared reference**
  Publish mappings as commons so they can be reused and adapted by other projects and communities.

Creation Process
----------------

The creation of maDMP mappings follows a collaborative workflow:

1. **Select a traditional DMP template**
   Identify the template to be converted into a machine-actionable format.

2. **Review standards and profiles**
   Familiarize yourself with the RDA maDMP Common Standard and the OSTrails Application Profile. Review existing mappings (e.g., Science Europe template).

3. **Draft the mapping**
   * Map sections and fields from the traditional template to maDMP components.
   * Define validation rules and controlled vocabularies (licenses, access levels, standards).
   * Request additions to the OSTrails AP if no corresponding field exists.

4. **Test usability**
   Validate the mapping with 3–5 real projects to ensure practical applicability.

5. **Publish as commons**
   The final mapping becomes part of the OSTrails commons and is available for reuse.


Integration
-----------

Once mappings are created, they can be integrated into DMP platforms and connected to RDM services such as:

* CRIS systems
* Data repositories
* PID systems

This integration enables automated workflows and ensures that DMPs remain accurate and up-to-date throughout the research lifecycle.
This work must be done by respective tool owners. The mappings are the relevant guidance for them that helps them achieve interoperability.


Mappings
-----------
Here we present the mappings identified for common DMP templates used across countries and thematic clusters.

.. toctree::
    :maxdepth: 1
    :titlesonly:

    Science Europe maDMP mapping <Science-Europe-maDMP-mapping>
    Austrian FWF – maDMP mapping <Austrian-FWF–maDMP-mapping>
