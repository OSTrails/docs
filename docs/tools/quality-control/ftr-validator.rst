FAIR FTR Schema Validator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FTR includes `ShEX and SHACL files <https://github.com/OSTrails/FAIR_testing_resource_vocabulary/tree/main/development>`_
for the different assessment components, allowing you to validate your
FTR records against this representation using any RDF validator tool,
such as `rudof <https://rudof-project.github.io/>`_.


A dedicated `FastAPI-based validation service <https://github.com/pabloalarconm/FAIR-assessment-record-validator>`_
is also available, wrapping **rudof** and exposing endpoints per entity type (``test``, ``testResult``,
``testResultSet``, ``metric``, ``benchmark``) and format (TTL or JSON-LD),
returning a structured validation report. It is fully containerized and ready to run with Docker.

    - **Persistent identifier**: not available yet
    - **Code repository**: https://github.com/pabloalarconm/FAIR-assessment-record-validator
    - **Version**: v0.3.0
    - **Release**: https://hub.docker.com/layers/pabloalarconm/fair-assessment-record-validator/0.3.0/
    - **License**: CC0 1.0 Universal
