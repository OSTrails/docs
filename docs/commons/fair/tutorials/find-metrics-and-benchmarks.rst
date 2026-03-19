.. _find-metrics-and-benchmarks:

Finding and Reusing Metrics and Benchmarks
==========================================

This tutorial explains how to discover FAIR metrics and benchmarks using
two complementary routes: the FAIRassist registry and FAIRsharing's own
search and browse features. Once you have found a metric of interest, you
can learn how to locate any tests that implement it in
`find-test-for-digital-object.rst <https://github.com/saracuriel/docs/blob/0ba068e8e83030cf3d168923a4f135a414f8167b/docs/commons/fair/tutorials/find-test-for-digital-object.rst>`_.

.. contents:: Contents
   :local:
   :depth: 2


What are metrics and benchmarks?
---------------------------------

FAIRsharing registers the conceptual components of the FAIR assessment
ecosystem within its FAIRassist registry. This includes:

- **Principles** — are designed to be subject- and implementation-agnostic criteria or high-level goals that may be refined for particular communities using the Assess IF (and are stored within FAIRsharing's
  Standards registry, e.g. the
  `FAIR Principles <https://doi.org/10.25504/FAIRsharing.WWI10U>`_).
- **Metrics** — measurable criteria that interpret a Principle,
  specifying what must be true of a digital object for that Principle to
  be satisfied.
- **Benchmarks** — curated sets of Metrics that together define what
  "FAIR" means in practice for a particular community, tool, or use case.
For more background on the FAIRassist registry and how it aligns with
the FAIR Testing Resource (FTR) vocabulary, see the
`FAIRsharing documentation on registry types
<https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/registry-type#fairassist>`_.


A note on object types
-----------------------

Both sections of this tutorial describe a number of ways to filter metrics and
benchmarks, including by the type of digital object they are designed to assess.
Before using this filter, it is worth reviewing the full controlled
vocabulary of object types in FAIRsharing, available at
`https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/object-types
<https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/object-types>`_.

The controlled vocabulary includes specific types such as dataset,
software application, model, terminology artifact, protocol or workflow,
and several others. Two general-purpose types are also available:

- *object type agnostic* — use this when a metric or benchmark is
  relevant across all types of digital object.
- *other object type* — use this only when the object type is not
  covered by any of the other terms in the vocabulary and the resource
  is not agnostic.

.. note::

   The term *object type not found* appears on a small number of older
   deprecated records where the original object type could not be
   determined during curation. This is an administrative term and is
   not relevant when searching for metrics or benchmarks; you can
   safely ignore it.

Take time to review the full vocabulary before selecting a type to
filter by, as the most appropriate choice may not always be immediately
obvious. For example, a metric that is relevant to all digital objects
should be found using *object type agnostic* rather than by listing
individual types.


Section 1: Metric discovery via FAIRassist
-------------------------------------------

The `FAIRassist registry <https://fairassist.org/registry>`_ is the
primary entry point for discovering metrics and benchmarks. Although
FAIRassist is part of FAIRsharing, its interface is purpose-built for
exploring these record types, and presents search results in a tabular
format that gives you an overview of the full ecosystem of resources
related to a given set of metrics or benchmarks.

FAIRassist is particularly useful for answering questions such as:

- What assessments already exist for my subject area or for a particular
  tool?
- Which standards and databases are referenced by assessments in my
  domain?
- What benchmarks has a given organisation defined or contributed to?
- Which metrics apply to a particular type of digital object?

This search and display method provides dynamic guidance that supplies extra context around FAIR
benchmarks, and transparent definitions of metrics to support their
correct reuse.


Using the filters
~~~~~~~~~~~~~~~~~

The FAIRassist registry provides five filters that can be used
individually or in combination.


Record type
^^^^^^^^^^^

Select whether you want to retrieve Metrics or Benchmarks (or both).
This is the broadest filter and must be used to ensure the appropriate usage of later filters.


Object type
^^^^^^^^^^^

Metrics can be filtered by the type of digital object they are designed
to assess. Before using this filter, review the full controlled
vocabulary of object types described in the `note on object types
<#a-note-on-object-types>`_ above and in the `FAIRsharing object types
documentation
<https://fairsharing.gitbook.io/fairsharing/record-sections-and-fields/general-information/object-types>`_,
to ensure you select the term that most accurately reflects your needs.
This may include *object type agnostic* for metrics that apply across
all digital object types, or *other object type* for those covering
object types not represented elsewhere in the vocabulary.


Tool
^^^^

Metrics can be filtered by the assessment tool that utilises them.
Currently available tool options include FOOPS! and FAIR Champion. This
filter is useful when you are working with a specific tool and want to
understand which metrics that tool draws on, or when you want to find
metrics that are already implemented in a tool you trust.


Subject
^^^^^^^

Both metrics and benchmarks can be filtered by subject area. The
subjects available reflect the FAIRsharing subject hierarchy, which you
can browse at `https://fairsharing.org/browse/subject
<https://fairsharing.org/browse/subject>`_. Use this filter to narrow
your results to metrics and benchmarks that are relevant to your
research domain.


Organisation
^^^^^^^^^^^^

Both metrics and benchmarks can be filtered by the organisation
associated with them. This is useful when you want to find all metrics
or benchmarks developed or maintained by a particular institution,
project, or working group.


A worked example: finding metrics linked to CESSDA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To illustrate how these filters work together, the following URL
retrieves all metrics associated with the CESSDA organisation and
linked to the FAIR Principles:

`https://fairassist.org/registry?search=(principle=The+FAIR+Principles%26organisations=cessda%26recordType=metric_ids <https://fairassist.org/registry?search=(principle=The+FAIR+Principles%26organisations=cessda%26recordType=metric_ids>`_

The results are displayed in tabular sections, one per record type,
allowing you to quickly scan the set of metrics that CESSDA has
contributed to or is associated with, alongside contextual information
about each one. From any row in the results you can navigate directly
to the full FAIRsharing record for that metric.


Section 2: Metric discovery via FAIRsharing
--------------------------------------------

FAIRsharing's own search and browse tools can also be used to find
metrics and benchmarks. This route is particularly useful when you want
to combine FAIRassist record types with other FAIRsharing filters, such
as status or object type, or when you want to use the advanced search to
build a precise query. Full documentation on FAIRsharing's search
features is available at
`https://fairsharing.gitbook.io/fairsharing/how-to/searching-and-browsing
<https://fairsharing.gitbook.io/fairsharing/how-to/searching-and-browsing>`_.


Simple search
~~~~~~~~~~~~~

The FAIRsharing simple search bar searches across all record types,
including metrics and benchmarks. Entering a keyword such as a FAIR
principle identifier, a domain term, or the name of a metric will return
all matching records. You can then use the faceted filters on the left of
the results page to narrow results to the FAIRassist registry, and
further refine by object type or a large number of other facets as required.


Advanced search
~~~~~~~~~~~~~~~

The advanced search gives you precise control over which record types,
statuses, object types, and fields are queried. For example, one or more object types
can be selected as part of the advanced search query construction,
allowing you to combine an object type filter with other criteria such
as record type, status, and associated tests. Before selecting an object
type, review the full controlled vocabulary described in the `note on
object types <#a-note-on-object-types>`_ above, to ensure you are using
the most appropriate term.

The following examples show how to retrieve specific subsets of
FAIRassist records.

To retrieve all metrics with a status of Ready or In Development:

`https://fairsharing.org/advancedsearch?operator=_and&fields=%28operator%3D_and%26fairassisttype%3Dmetric%26status%3Dready%2Bin_development%29 <https://fairsharing.org/advancedsearch?operator=_and&fields=%28operator%3D_and%26fairassisttype%3Dmetric%26status%3Dready%2Bin_development%29>`_

To retrieve all benchmarks with a status of Ready or In Development:

`https://fairsharing.org/advancedsearch?operator=_and&fields=%28operator%3D_and%26fairassisttype%3Dbenchmark%26status%3Dready%2Bin_development%29 <https://fairsharing.org/advancedsearch?operator=_and&fields=%28operator%3D_and%26fairassisttype%3Dbenchmark%26status%3Dready%2Bin_development%29>`_

To retrieve all Ready or In Development metrics that have at least one
associated test — a useful starting point if you are looking for metrics
that are already implemented and ready for use:

`https://fairsharing.org/advancedsearch?operator=_and&fields=%28operator%3D_and%26fairassisttype%3Dmetric%26status%3Dready%2Bin_development%26associatedTests%3Dtrue%29 <https://fairsharing.org/advancedsearch?operator=_and&fields=%28operator%3D_and%26fairassisttype%3Dmetric%26status%3Dready%2Bin_development%26associatedTests%3Dtrue%29>`_


Browse by subject
~~~~~~~~~~~~~~~~~

If you prefer to explore visually, the FAIRsharing subject browser at
`https://fairsharing.org/browse/subject <https://fairsharing.org/browse/subject>`_
allows you to navigate a hierarchical sunburst diagram of subject areas.
Selecting a subject will show you all FAIRsharing records tagged with
that subject or any of its child terms, across all registries including
FAIRassist.


Next steps
----------

Once you have identified a metric of interest, you may want to find any
tests that implement it. See `find-test-for-digital-object.rst <https://github.com/saracuriel/docs/blob/0ba068e8e83030cf3d168923a4f135a414f8167b/docs/commons/fair/tutorials/find-test-for-digital-object.rst>`_ for a
step-by-step guide.


