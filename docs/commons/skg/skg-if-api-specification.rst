OSTrails SKG-IF API Specification
==================================

The SKG-IF OpenAPI specification defines a common way to programmatically interact with Scholarly Knowledge Graph (SKG) providers and related services. The API enables uniform access to SKG information and operations, even when individual implementations differ in their internal architectures, technology stacks, or integration patterns.

Purpose and design principles
-------------------------------

The SKG-IF API specifications are designed so as to:

* Provide a standardised REST/OpenAPI interface for SKG-IF entities (research products, agents, venues, data sources, grants, topics);
* Support machine-to-machine interoperability in heterogeneous environments;
* Decouple external interactions from internal data models and storage technologies;
* Facilitate validation, testing, and automation of SKG-IF–based workflows.


The specification focuses on the shape and semantics of the JSON responses and operations, not on how services internally manage or persist data. This enables the independent evolution of local systems while maintaining a predictable, interoperable way for exchanging data.

Relationship to the data model and JSON-LD
---------------------------------------------

The SKG-IF OpenAPI builds directly on the SKG-IF Data Model and the SKG-IF JSON-LD context. In particular:

* Single-entity operations (`/{entity-type}/{local_identifier}`) return JSON that is compatible with the SKG-IF JSON-LD context (via `@context`), and **must** conform to the OpenAPI response schemas.
* Search operations (`/{entity-type}?filter=…`) return JSON-only responses with a `meta` object and a `results` array; work is in progress to provide an appropriate JSON-LD context pattern for paged/search results.

The specification defines how key SKG-IF concepts, such as `local_identifier`, `entity_type`, and identifiers (DOI, ORCID, ROR, etc.), as well as embedded entities (e.g., agents and venues within products), are exposed via the API.

Uniform operations and validation across implementations
---------------------------------------------------------

By implementing the SKG-IF OpenAPI, SKG-IF providers can expose a consistent set of operations, such as:

* Retrieving a single entity by `local_identifier`,
* Searching entities using filter expressions,
* Serving JSON-LD–compatible representations for core SKG-IF entities.

Implementations can be automatically validated against the SKG-IF OpenAPI specification using a validation proxy such as Stoplight Prism. A typical validation setup:

1. Download the SKG-IF OpenAPI YAML file: https://skg-if.github.io/api/openapi/ver/current/skg-if-openapi.yaml
2. Run a Prism proxy in front of your implementation, e.g.: docker run --init --rm -v $(pwd):/tmp -p 4010:4010 stoplight/prism:4 proxy -h 0.0.0.0 /tmp/skg-if-openapi.yaml http://my-dev-server:8080 --errors
3. Exercise your endpoints through the proxy (e.g., http://localhost:4010/products) and use the proxy responses to detect schema and contract violations.

This validation approach can be integrated into CI/CD pipelines. If an implementation passes the OpenAPI conformance tests, it is considered compliant with SKG-IF at the API level; SHACL validation is not required in addition to OpenAPI compliance.

Community governance and maintenance
-------------------------------------

The SKG-IF OpenAPI specification is developed and maintained collaboratively within the RDA SKG-IF Working Group and its broader implementer community. Discussion and feedback loops are driven by concrete implementation experience (e.g., hackathons, pilot deployments) and captured in public issue trackers and documents.

Relevant community resources include:

    * SKG-IF OpenAPI YAML (“current” dev version): https://skg-if.github.io/api/openapi/ver/current/skg-if-openapi.yaml
    * GitHub source (current): https://raw.githubusercontent.com/skg-if/api/refs/heads/main/openapi/ver/current/skg-if-openapi.yaml
    * Permanent alias for the current version: https://w3id.org/skg-if/api/skg-if-openapi.yaml
    * General API repository:  https://github.com/skg-if/api
    * RDA SKG-IF WG and implementer channel on Discord.

These venues are the authoritative places to report issues, discuss design choices (e.g., filter grammar, JSON-LD options, authentication strategies), and propose enhancements.

Documentation and versioning
-----------------------------

The SKG-IF OpenAPI specification is published as a machine-readable OpenAPI document and can be explored through multiple viewers:

    * Stoplight Elements: https://elements-demo.stoplight.io/?spec=https://skg-if.github.io/api/openapi/ver/current/skg-if-openapi.yaml
    * Redocly Redoc: https://redocly.github.io/redoc/?url=https://skg-if.github.io/api/openapi/ver/current/skg-if-openapi.yaml
    * Swagger Editor https://editor-next.swagger.io with input https://skg-if.github.io/api/openapi/ver/current/skg-if-openapi.yaml

Versioning follows a clear separation between the SKG-IF Data Model / JSON-LD context version (e.g., `https://w3id.org/skg-if/context/1.0.1/skg-if.json`), and the **SKG-IF OpenAPI** version, using semantic versioning in `info.version` (e.g., `1.1.3`), with the rule that major versions of the data model and the OpenAPI should always match.

Examples:
---------

    * Official released OpenAPI version: https://github.com/skg-if/api/openapi/ver/1.1.3/skg-if-openapi.yaml
    * Permanent URL:  https://w3id.org/skg-if/api/1.1.3/skg-if-openapi.yaml
    * Data Model / context versions:  https://w3id.org/skg-if/context/1.0.0/skg-if.json, and https://w3id.org/skg-if/context/1.0.1/skg-if.json
    * Current alias: https://w3id.org/skg-if/context/skg-if.json

The specification evolves iteratively, incorporating feedback from real-world implementations (e.g., on filters, extensions, missing fields, JSON-LD behaviour). Future versions aim to maintain compatibility with the SKG-IF Data Model while providing a stable yet extensible API surface for the SKG Commons.

