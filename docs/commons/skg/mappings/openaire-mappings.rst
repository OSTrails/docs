OpenAIRE SKG-IF Mapping
-----------------------------------------
..  page-authors::
    Miriam Baglioni



This page documents the conceptual mapping between the `OpenAIRE Graph model <https://graph.openaire.eu/doc/data-model>`_  towards the `SKG-IF <https://skg-if.github.io/interoperability-framework/>`_ (`version 1.1.0 <https://github.com/skg-if/context/tree/main/ver/1.1.0>`_).

The OpenAIRE APIs implementation draws from this mapping. The mapped entities reported are only those returned by the APIs. So far only research products.

Research Product
===============================================

.. list-table::
   :header-rows: 1

   * - SKG-IF JSON-LD property
     - OpenAIRE Graph property
     - Notes

   * - https://skg-if.github.io/interoperability-framework/docs/research-product.html#local_identifier
     - https://graph.openaire.eu/docs/data-model/entities/research-product#id
     - The internal identifier is used to resolve to the landing page in Explore for the research product. The URL prefix "https://explore.openaire.eu/search/result?id=" is added to the result identifier.

   * - https://skg-if.github.io/interoperability-framework/docs/research-product.html#identifiers
     - https://graph.openaire.eu/docs/data-model/entities/research-product#pids
     -

   * - https://skg-if.github.io/interoperability-framework/docs/research-product.html#entity_type
     - product
     - Fixed value

   * - https://skg-if.github.io/interoperability-framework/docs/research-product.html#titles
     - https://graph.openaire.eu/docs/data-model/entities/research-product#maintitle or https://graph.openaire.eu/docs/data-model/entities/research-product#subtitle
     - Maps the first title with type *main title*. If no *main title* exists, it maps the first *subtitle*. The element always has *none* as language keyword.

   * - https://skg-if.github.io/interoperability-framework/docs/research-product.html#abstracts
     - https://graph.openaire.eu/docs/data-model/entities/research-product#descriptions
     - Maps the whole set of descriptions. All of them are associated with the language tag *none*.

   * - https://skg-if.github.io/interoperability-framework/docs/research-product.html#product_type
     - https://graph.openaire.eu/docs/data-model/entities/research-product#sub-types
     - |
       The sub-types are mapped in the SKG-IF as:

       - publication → literature
       - dataset → research data
       - software → research software
       - otherresearchproduct → other

   * - https://skg-if.github.io/interoperability-framework/docs/research-product.html#topics
     - https://graph.openaire.eu/docs/data-model/entities/research-product#subjects
     - |
       The mapping considers *{FOS, SDG, keyword}* subject schemes. Each subfield is mapped as follows:

       - term -> otf identifier depending on the creation date of the dataset, and the value for the topic
       - **provenance**
         - trust -> subject.provenance.trust
         - provenance -> subject.provenance.provenance

   * - https://skg-if.github.io/interoperability-framework/docs/research-product.html#contributions
     - https://graph.openaire.eu/docs/data-model/entities/research-product#authors
     - |
       Each subfield is mapped as follows:

       - by -> otf identifier depending on the creation date of the dataset and the ORCID if found in the metadata. If no ORCID is found, the identifier depends on the creation date and a concatenation of result ID and author position in the list of authors.
       - declared_affiliations -> not mapped so far
       - rank -> author[*].rank
       - contribution_types -> not mapped so far
       - role -> author

   * - https://skg-if.github.io/interoperability-framework/docs/research-product.html#manifestations
     - https://graph.openaire.eu/docs/data-model/entities/research-product#instances, https://graph.openaire.eu/docs/data-model/entities/research-product#container, and https://graph.openaire.eu/docs/data-model/relationships/relationship-object
     - |
       Each subfield is mapped as follows:

       - **type**
         - class -> the COAR classification for instance[*].type
         - labels -> instances[*].type (language keyword always *en*)
         - defined_in -> https://vocabularies.coar-repositories.org/resource_types/ (Fixed)
       - dates -> instance.publicationDate (date type always *publication*)
       - identifiers -> instances[*].pids
       - **peer_review**
         - status -> set to *peer reviewed* if instances[*].refereed is *peer reviewed*
         - description -> not mapped so far
       - **access_right**
         - status -> instances[*].accessright.label
         - description -> fixed text depending on status value
       - licence -> instances[*].licence
       - version -> not mapped
       - **biblio**
         - issue -> container.iss (only for publications)
         - edition -> container.edition (only for publications)
         - volume -> container.volume (only for publications)
         - pages -> container.sp and container.ep (only for publications)
         - in -> otf identifier depending on the creation date and container.issnPrinted. If not present, container.issnOnline is used
         - hosting_datasource -> "https://explore.openaire.eu/search/dataprovider?datasourceId=" + target in the relation isHostedBy

   * - https://skg-if.github.io/interoperability-framework/docs/research-product.html#relevant_organisations
     - https://graph.openaire.eu/docs/data-model/relationships/relationship-object
     - The list of landing pages in OpenAIRE built from organization identifiers found in *relation.source* for relations with *relation.relType.name = isAuthorInstitutionOf* and *relation.target* as the considered result

   * - https://skg-if.github.io/interoperability-framework/docs/research-product.html#funding
     - https://graph.openaire.eu/docs/data-model/relationships/relationship-object
     - The list of landing pages in OpenAIRE built from project identifiers found in *relation.source* for relations with *relation.relType.name = produces* and *relation.target* as the considered result

   * - https://skg-if.github.io/interoperability-framework/docs/research-product.html#related_products
     - https://graph.openaire.eu/docs/data-model/relationships/relationship-object
     - For each supported semantics in SKG-IF, the corresponding semantics in the OpenAIRE graph is considered. For any relation type, the list of landing pages in OpenAIRE is built from *relation.target* relations having as *relation.source* the result under consideration