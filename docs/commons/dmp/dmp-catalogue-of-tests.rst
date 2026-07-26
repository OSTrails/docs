Catalogue of Tests
==================

.. page-authors::


The following catalogue lists the 105 DMP Tests defined within the OSTrails project, implementing the metrics described in :doc:`DMP Evaluation Metrics <dmp-evaluation-metrics>`.


.. list-table::
   :header-rows: 1
   :class: small-table

   * - No.
     - Test ID
     - Title
   * - 1
     - T-DCSC-001
     - :ref:`Check for reused dataset declaration <dmp-test-1>`
   * - 2
     - T-DCSC-002
     - :ref:`Check License for Reused Datasets <dmp-test-2>`
   * - 3
     - T-DCSC-003
     - :ref:`Check for reused dataset PID <dmp-test-3>`
   * - 4
     - T-DCSC-004
     - :ref:`Check Distribution Entry is Present <dmp-test-4>`
   * - 5
     - T-DCSC-005
     - :ref:`Check Distribution Access Information is Present <dmp-test-5>`
   * - 6
     - T-DCSC-006
     - :ref:`Check Distribution Title is Present <dmp-test-6>`
   * - 7
     - T-DCSC-007
     - :ref:`Check Access Rights for Reused Datasets <dmp-test-7>`
   * - 8
     - T-DCSC-008
     - :ref:`Check Personal Data Flag for Reused Datasets <dmp-test-8>`
   * - 9
     - T-DCSC-009
     - :ref:`Check Sensitive Data Flag for Reused Datasets <dmp-test-9>`
   * - 10
     - T-DCSC-010
     - :ref:`Check Distribution URL is Present <dmp-test-10>`
   * - 11
     - T-DCSC-011
     - :ref:`Check Access URL is Present and Non-empty <dmp-test-11>`
   * - 12
     - T-DCSC-012
     - :ref:`Check PID Matches Destination Repository Record <dmp-test-12>`
   * - 13
     - T-DCSC-013
     - :ref:`Check PID Resolves Successfully <dmp-test-13>`
   * - 14
     - T-DCSC-014
     - :ref:`Check Reused Data Access Matches Destination <dmp-test-14>`
   * - 15
     - T-DCSC-015
     - :ref:`Check Reused Data License Matches Destination <dmp-test-15>`
   * - 16
     - T-DCSC-016
     - :ref:`Check for new data (no is_reused) <dmp-test-16>`
   * - 17
     - T-DCSC-017
     - :ref:`Check technical_resource for new data collection/creation <dmp-test-17>`
   * - 18
     - T-DCSC-018
     - :ref:`Check data_access for new datasets <dmp-test-18>`
   * - 19
     - T-DCSC-019
     - :ref:`Check rights of new dataset <dmp-test-19>`
   * - 20
     - T-DCSC-020
     - :ref:`Check metadata for new dataset <dmp-test-20>`
   * - 21
     - T-DCSC-021
     - :ref:`Check dataset_id exists <dmp-test-21>`
   * - 22
     - T-DCSC-022
     - :ref:`Check PID resolves for dataset_id <dmp-test-22>`
   * - 23
     - T-DCSC-023
     - :ref:`Check new data access matches destination <dmp-test-23>`
   * - 24
     - T-DCSC-024
     - :ref:`Check new data license matches destination <dmp-test-24>`
   * - 25
     - T-DCSC-025
     - :ref:`Check dataset.type is specified <dmp-test-25>`
   * - 26
     - T-DCSC-026
     - :ref:`Check distribution.format is specified <dmp-test-26>`
   * - 27
     - T-DCSC-027
     - :ref:`Check distribution.byte_size is specified <dmp-test-27>`
   * - 28
     - T-DCSC-028
     - :ref:`Check dataset.type matches destination type <dmp-test-28>`
   * - 29
     - T-DCSC-029
     - :ref:`Check dataset.type aligns with destination subtype <dmp-test-29>`
   * - 30
     - T-DCSC-030
     - :ref:`Check final dataset format matches destination files <dmp-test-30>`
   * - 31
     - T-DCSC-031
     - :ref:`Check final dataset size matches destination size <dmp-test-31>`
   * - 32
     - T-DCSC-032
     - :ref:`Check maDMP JSON Validates Against DMP Common Standard Schema <dmp-test-32>`
   * - 33
     - T-DCSC-033
     - :ref:`Check dataset_methodology for controlled vocabularies <dmp-test-33>`
   * - 34
     - T-DCSC-034
     - :ref:`Check technical_resource.name for electronic lab notebook reference <dmp-test-34>`
   * - 35
     - T-DCSC-035
     - :ref:`Check related_identifier resource_type for ReadMe file <dmp-test-35>`
   * - 36
     - T-DCSC-036
     - :ref:`Check metadata_standard_id is registered in metadata registries <dmp-test-36>`
   * - 37
     - T-DCSC-037
     - :ref:`Check distribution format is open <dmp-test-37>`
   * - 38
     - T-DCSC-038
     - :ref:`Check ELN dataset linked via related_ids <dmp-test-38>`
   * - 39
     - T-DCSC-039
     - :ref:`Check technical_resource for dataset documentation <dmp-test-39>`
   * - 40
     - T-DCSC-040
     - :ref:`Check data_quality_assurance for quality control methods <dmp-test-40>`
   * - 41
     - T-DCSC-041
     - :ref:`Check host.title and host.url for storage location <dmp-test-41>`
   * - 42
     - T-DCSC-042
     - :ref:`Check host for trusted repository storage <dmp-test-42>`
   * - 43
     - T-DCSC-043
     - :ref:`Check sensitive_data classification is assigned <dmp-test-43>`
   * - 44
     - T-DCSC-044
     - :ref:`Check host security and backup reflect sensitivity level <dmp-test-44>`
   * - 45
     - T-DCSC-045
     - :ref:`Check contributor.role for backup responsibility <dmp-test-45>`
   * - 46
     - T-DCSC-046
     - :ref:`Check backup_frequency is declared <dmp-test-46>`
   * - 47
     - T-DCSC-047
     - :ref:`Check host.id matches Zenodo deposit location <dmp-test-47>`
   * - 48
     - T-DCSC-048
     - :ref:`Check security_and_privacy.title for security measures <dmp-test-48>`
   * - 49
     - T-DCSC-049
     - :ref:`Check security_and_privacy.description for access rights management <dmp-test-49>`
   * - 50
     - T-DCSC-050
     - :ref:`Check security_and_privacy.description for authorised access controls <dmp-test-50>`
   * - 51
     - T-DCSC-051
     - :ref:`Check security_and_privacy.description for access control and user permissions <dmp-test-51>`
   * - 52
     - T-DCSC-052
     - :ref:`Check security_and_privacy.description for access procedures <dmp-test-52>`
   * - 53
     - T-DCSC-053
     - :ref:`Check security_and_privacy.description and ethical_issues_report for GDPR and ethics compliance <dmp-test-53>`
   * - 54
     - T-DCSC-054
     - :ref:`Check security_and_privacy.title for implemented security measures at destination <dmp-test-54>`
   * - 55
     - T-DCSC-055
     - :ref:`Check security_and_privacy.description for data protection method when sensitive_data is true <dmp-test-55>`
   * - 56
     - T-DCSC-056
     - :ref:`Check security_and_privacy for anonymised synthetic data provision <dmp-test-56>`
   * - 57
     - T-DCSC-057
     - :ref:`Check rights for statement of no data restrictions <dmp-test-57>`
   * - 58
     - T-DCSC-058
     - :ref:`Check license_ref for dataset licence <dmp-test-58>`
   * - 59
     - T-DCSC-059
     - :ref:`Check license_ref against SPDX for software datasets <dmp-test-59>`
   * - 60
     - T-DCSC-060
     - :ref:`Check data_access and rights for access agreements or MoUs <dmp-test-60>`
   * - 61
     - T-DCSC-061
     - :ref:`Check contributor.role for data owner <dmp-test-61>`
   * - 62
     - T-DCSC-062
     - :ref:`Check contributor for author role when dataset type is software <dmp-test-62>`
   * - 63
     - T-DCSC-063
     - :ref:`Check ethical_issues_exist for valid value <dmp-test-63>`
   * - 64
     - T-DCSC-064
     - :ref:`Check ethical_issues_description is present when ethical_issues_exist is no <dmp-test-64>`
   * - 65
     - T-DCSC-065
     - :ref:`Check data_access for open status <dmp-test-65>`
   * - 66
     - T-DCSC-066
     - :ref:`Check distribution is present for dataset <dmp-test-66>`
   * - 67
     - T-DCSC-067
     - :ref:`Check license_ref is present within distribution <dmp-test-67>`
   * - 68
     - T-DCSC-068
     - :ref:`Check rights for data restrictions reference <dmp-test-68>`
   * - 69
     - T-DCSC-069
     - :ref:`Check distribution license_ref for Horizon Europe CC-BY compliance <dmp-test-69>`
   * - 70
     - T-DCSC-070
     - :ref:`Check data_access matches destination host access policy <dmp-test-70>`
   * - 71
     - T-DCSC-071
     - :ref:`Check distribution license_ref matches destination host licence policy <dmp-test-71>`
   * - 72
     - T-DCSC-072
     - :ref:`Check distribution license.start_date matches destination embargo policy <dmp-test-72>`
   * - 73
     - T-DCSC-073
     - :ref:`Check rights matches destination host restriction policy <dmp-test-73>`
   * - 74
     - T-DCSC-074
     - :ref:`Check repository host for absence of embargo date <dmp-test-74>`
   * - 75
     - T-DCSC-075
     - :ref:`Check distribution.license.start_date for absence in maDMP <dmp-test-75>`
   * - 76
     - T-DCSC-076
     - :ref:`Check host.title and host.url against thematic repository registries <dmp-test-76>`
   * - 77
     - T-DCSC-077
     - :ref:`Check host against OpenAIRE and FAIRsharing FAIR benchmarks <dmp-test-77>`
   * - 78
     - T-DCSC-078
     - :ref:`Check host against trusted repository registry benchmark <dmp-test-78>`
   * - 79
     - T-DCSC-079
     - :ref:`Check host.backup_frequency and host.backup_type for back-up strategy <dmp-test-79>`
   * - 80
     - T-DCSC-080
     - :ref:`Check certified_with exists in host <dmp-test-80>`
   * - 81
     - T-DCSC-081
     - :ref:`Check cost title or description for preservation reference <dmp-test-81>`
   * - 82
     - T-DCSC-082
     - :ref:`Check host_id against FAIRsharing for repository policy <dmp-test-82>`
   * - 83
     - T-DCSC-083
     - :ref:`Check dataset_id resolves to declared destination via DOI URL <dmp-test-83>`
   * - 84
     - T-DCSC-084
     - :ref:`Check preservation_statement and host for long-term storage intention <dmp-test-84>`
   * - 85
     - T-DCSC-085
     - :ref:`Check dataset.keyword against Zenodo keywords <dmp-test-85>`
   * - 86
     - T-DCSC-086
     - :ref:`Check dataset.language against Zenodo language support <dmp-test-86>`
   * - 87
     - T-DCSC-087
     - :ref:`Check host_id against Zenodo and FAIRsharing for policy compliance <dmp-test-87>`
   * - 88
     - T-DCSC-088
     - :ref:`Check related_identifier.identifier for external resources <dmp-test-88>`
   * - 89
     - T-DCSC-089
     - :ref:`Check related_identifier for metadata standard fields <dmp-test-89>`
   * - 90
     - T-DCSC-090
     - :ref:`Check URLs in maDMP are valid and resolvable <dmp-test-90>`
   * - 91
     - T-DCSC-091
     - :ref:`Check dataset fields against OpenAIRE SKG-IF API <dmp-test-91>`
   * - 92
     - T-DCSC-092
     - :ref:`Check contributor roles against CRediT taxonomy <dmp-test-92>`
   * - 93
     - T-DCSC-093
     - :ref:`Check host.pid_system for PID declaration <dmp-test-93>`
   * - 94
     - T-DCSC-094
     - :ref:`Check certified_with against trusted registry <dmp-test-94>`
   * - 95
     - T-DCSC-095
     - :ref:`Check host_id.identifier and host_id.type for valid repository link <dmp-test-95>`
   * - 96
     - T-DCSC-096
     - :ref:`Check host.pid_system matches destination PID system in Zenodo <dmp-test-96>`
   * - 97
     - T-DCSC-097
     - :ref:`Check dmp.contributor name, role, and contact <dmp-test-97>`
   * - 98
     - T-DCSC-098
     - :ref:`Check dmp.contributor.role for Data Steward <dmp-test-98>`
   * - 99
     - T-DCSC-099
     - :ref:`Check contributor_id and affiliation.affiliation_id for PIDs <dmp-test-99>`
   * - 100
     - T-DCSC-100
     - :ref:`Check dmp.contributor fields against destination contributors <dmp-test-100>`
   * - 101
     - T-DCSC-101
     - :ref:`Check Data Steward role in maDMP against contributors.type Other in destination <dmp-test-101>`
   * - 102
     - T-DCSC-102
     - :ref:`Check contributor PIDs in maDMP against Zenodo contributors <dmp-test-102>`
   * - 103
     - T-DCSC-103
     - :ref:`Check cost in maDMP against repository cost <dmp-test-103>`
   * - 104
     - T-DCSC-104
     - :ref:`Check cost fields for budget specification <dmp-test-104>`
   * - 105
     - T-DCSC-105
     - :ref:`Check cost in maDMP for no additional resources statement <dmp-test-105>`


----

.. _dmp-test-1:

Test 1: Check for reused dataset declaration
--------------------------------------------

:Test ID: T-DCSC-001
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-001
:Implements: :ref:`Metric 1: Reused Dataset Declared in the DMP <data.reused.co.1>`

Description
^^^^^^^^^^^

Given a maDMP JSON document, inspect dataset objects and verify the presence of a field indicating whether the dataset is reused.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries.
3. Check whether at least one dataset contains `is_reused`.
4. If present, return pass; otherwise return fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-001",
        "@type": "ftr:Test",
        "dcterms:identifier": "madmp-reused-datasets-declared-json",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check for reused dataset declaration"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Given a maDMP JSON document, inspect dataset objects and verify the presence of a field indicating whether the dataset is reused."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "reused dataset"
          },
          {
            "@language": "en",
            "@value": "data reuse"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          },
          {
            "@language": "en",
            "@value": "completeness"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.co.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-2:

Test 2: Check License for Reused Datasets
-----------------------------------------

:Test ID: T-DCSC-002
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-002
:Implements: :ref:`Metric 3: Reused Dataset Has a Declared License <data.reused.co.3>`

Description
^^^^^^^^^^^

Checks whether the `is_reused` dataset entry includes a license reference (`license_ref`) with both a license identifier and a start date, confirming that the legal terms for reusing the dataset are declared.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate all dataset entries.
3. Select datasets where `is_reused = true`.
4. Verify that a `license` object exists.
5. Verify that `license.ref` exists and is non-empty.
6. Optionally verify that `license.start_date` exists.
7. If all reused datasets comply, return pass; otherwise return fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-002",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check License for Reused Datasets"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Check if `is_reused` includes license (ref and start_date)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "reused dataset"
          },
          {
            "@language": "en",
            "@value": "data license"
          },
          {
            "@language": "en",
            "@value": "license reference"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.co.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-3:

Test 3: Check for reused dataset PID
------------------------------------

:Test ID: T-DCSC-003
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-003
:Implements: :ref:`Metric 2: Reused Dataset Has a Persistent Identifier <data.reused.co.2>`

Description
^^^^^^^^^^^

Checks whether the `is_reused` dataset entry includes a persistent identifier (`dataset_id`) with both an identifier value and a type, confirming that the reused dataset can be unambiguously referenced.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate all dataset entries.
3. Select datasets where `is_reused = true`.
4. Verify that `dataset_id.identifier` exists and is non-empty.
5. Optionally verify that `dataset_id.type` exists.
6. If all reused datasets comply, return pass; otherwise return fail.
7. If no reused datasets exist, return not applicable (optional policy).

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-003",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check for reused dataset PID"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the reused dataset entry includes a persistent identifier with both an identifier value and type, confirming the dataset can be unambiguously referenced."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "reused dataset"
          },
          {
            "@language": "en",
            "@value": "persistent identifier"
          },
          {
            "@language": "en",
            "@value": "PID"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.co.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-4:

Test 4: Check Distribution Entry is Present
-------------------------------------------

:Test ID: T-DCSC-004
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-004
:Implements: :ref:`Metric 4: Reused Dataset Has Distribution Information <data.reused.co.4>`

Description
^^^^^^^^^^^

Checks whether at least one distribution entry exists for the dataset, confirming that information about how and where the data is accessible has been provided in the maDMP.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate all dataset entries.
3. Select datasets where `is_reused = true`.
4. Verify that a `distribution` (or equivalent) object or array exists.
5. If all reused datasets contain distribution metadata, return pass; otherwise return fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-004",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check Distribution Entry is Present"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether at least one distribution entry exists for the dataset, confirming that information about how and where the data is accessible has been provided."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "reused dataset"
          },
          {
            "@language": "en",
            "@value": "data distribution"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          },
          {
            "@language": "en",
            "@value": "completeness"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.co.4"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-5:

Test 5: Check Distribution Access Information is Present
--------------------------------------------------------

:Test ID: T-DCSC-005
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-005
:Implements: :ref:`Metric 4: Reused Dataset Has Distribution Information <data.reused.co.4>`

Description
^^^^^^^^^^^

Checks whether distribution includes access information (e.g., access URL or download URL).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate reused datasets (`is_reused = true`).
3. For each distribution, verify that at least one access field exists (e.g., `access_url`, `download_url`, or equivalent).
4. If all reused datasets contain access information, return pass; otherwise return fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-005",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check Distribution Access Information is Present"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether distribution includes access information (e.g., access URL or download URL)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "reused dataset"
          },
          {
            "@language": "en",
            "@value": "data access"
          },
          {
            "@language": "en",
            "@value": "distribution"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.co.4"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-6:

Test 6: Check Distribution Title is Present
-------------------------------------------

:Test ID: T-DCSC-006
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-006
:Implements: :ref:`Metric 4: Reused Dataset Has Distribution Information <data.reused.co.4>`

Description
^^^^^^^^^^^

Checks whether the distribution entry includes a non-empty title, confirming that the distribution is named and can be identified by users browsing the dataset record.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate reused datasets (`is_reused = true`).
3. For each distribution, verify that a non-empty `title` field exists.
4. If all reused datasets contain a title, return pass; otherwise return fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-006",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check Distribution Title is Present"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the distribution entry includes a non-empty title, confirming that the distribution is named and identifiable."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "reused dataset"
          },
          {
            "@language": "en",
            "@value": "distribution title"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          },
          {
            "@language": "en",
            "@value": "completeness"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.co.4"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-7:

Test 7: Check Access Rights for Reused Datasets
-----------------------------------------------

:Test ID: T-DCSC-007
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-007
:Implements: :ref:`Metric 5: Reused Dataset Has Declared Access Conditions <data.reused.co.5>`

Description
^^^^^^^^^^^

Checks whether the data access field (`data_access`) for the reused dataset is declared with a recognised value — open, shared, or closed — confirming that access conditions are explicitly stated.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate all dataset entries.
3. Select datasets where `is_reused = true`.
4. Verify that `data_access` exists.
5. Verify that its value is one of: `open`, `shared`, `closed`.
6. If all reused datasets comply, return pass; otherwise return fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-007",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check Access Rights for Reused Datasets"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the data access field for the reused dataset is declared with a recognised value — open, shared, or closed."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "reused dataset"
          },
          {
            "@language": "en",
            "@value": "access rights"
          },
          {
            "@language": "en",
            "@value": "data access"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.co.5"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-8:

Test 8: Check Personal Data Flag for Reused Datasets
----------------------------------------------------

:Test ID: T-DCSC-008
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-008
:Implements: :ref:`Metric 6: Reused Dataset Contains Personal Data <data.reused.co.6>`

Description
^^^^^^^^^^^

Checks whether the `personal_data` field is present and populated for the reused dataset entry, confirming that the DMP addresses whether the data contains personal information subject to data protection regulations.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate all dataset entries.
3. Select datasets where `is_reused = true`.
4. Verify that `personal_data` exists.
5. Verify that its value is explicit and valid (e.g., `true/false`, or a controlled term your schema allows).
6. If all reused datasets comply, return pass; otherwise return fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-008",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check Personal Data Flag for Reused Datasets"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the personal_data field is present and populated, confirming the DMP addresses whether the data contains personal information."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "personal data"
          },
          {
            "@language": "en",
            "@value": "data protection"
          },
          {
            "@language": "en",
            "@value": "reused dataset"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.co.6"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-9:

Test 9: Check Sensitive Data Flag for Reused Datasets
-----------------------------------------------------

:Test ID: T-DCSC-009
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-009
:Implements: :ref:`Metric 7: Reused Dataset Contains Sensitive Data <data.reused.co.7>`

Description
^^^^^^^^^^^

Checks whether the `sensitive_data` field is present and populated for the reused dataset entry, confirming that the DMP addresses whether the data requires special handling or protection measures.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate all dataset entries.
3. Select datasets where `is_reused = true`.
4. Verify that `sensitive_data` exists.
5. Verify that its value is explicit and valid.
6. If all reused datasets comply, return pass; otherwise return fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-009",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check Sensitive Data Flag for Reused Datasets"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the sensitive_data field is present and populated, confirming the DMP addresses whether the data requires special handling."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "sensitive data"
          },
          {
            "@language": "en",
            "@value": "data security"
          },
          {
            "@language": "en",
            "@value": "reused dataset"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.co.7"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-10:

Test 10: Check Distribution URL is Present
------------------------------------------

:Test ID: T-DCSC-010
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-010
:Implements: :ref:`Metric 8: Reused Dataset Has an Access URL <data.reused.co.8>`

Description
^^^^^^^^^^^

Checks whether a distribution entry with an access URL is present for the reused dataset, confirming that users can locate and retrieve the data from a declared address.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate reused datasets (`is_reused = true`).
3. Verify that at least one distribution object exists.
4. If yes, return pass; otherwise return fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-010",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check Distribution URL is Present"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether a distribution entry with an access URL is present for the reused dataset, confirming users can locate and retrieve the data."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "reused dataset"
          },
          {
            "@language": "en",
            "@value": "access URL"
          },
          {
            "@language": "en",
            "@value": "data location"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.co.8"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-11:

Test 11: Check Access URL is Present and Non-empty
--------------------------------------------------

:Test ID: T-DCSC-011
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-011
:Implements: :ref:`Metric 8: Reused Dataset Has an Access URL <data.reused.co.8>`

Description
^^^^^^^^^^^

Checks whether the `access_url` field within the distribution entry is present and non-empty, confirming that a direct link to the data is provided in the maDMP.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate reused datasets (`is_reused = true`).
3. Verify that at least one distribution contains `access_url`.
4. If yes, return pass; otherwise return fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-011",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check Access URL is Present and Non-empty"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the access_url field within the distribution entry is present and non-empty, confirming a direct link to the data is provided."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "access URL"
          },
          {
            "@language": "en",
            "@value": "data location"
          },
          {
            "@language": "en",
            "@value": "distribution"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.co.8"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-12:

Test 12: Check PID Matches Destination Repository Record
--------------------------------------------------------

:Test ID: T-DCSC-012
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-012
:Implements: :ref:`Metric 9: Reused Dataset PID Resolves in the Repository <data.reused.feas.1>`

Description
^^^^^^^^^^^

Checks whether the persistent identifier declared for the reused dataset in the maDMP matches the corresponding record found in the destination repository, confirming consistency between the plan and the repository.

Input
^^^^^

- dataset_id in maDMP
- repository identifier field(s) (e.g., DOI URL)

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Extract reused dataset identifiers from maDMP (`is_reused = true`).
2. Query the target repository using the identifier.
3. Retrieve the repository’s canonical identifier for the record.
4. Compare with the maDMP dataset identifier.
5. Pass if all identifiers match a repository record; otherwise fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-012",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check PID Matches Destination Repository Record"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if reused dataset id in DMP matches the destination."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "persistent identifier"
          },
          {
            "@language": "en",
            "@value": "PID"
          },
          {
            "@language": "en",
            "@value": "repository"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.feas.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-13:

Test 13: Check PID Resolves Successfully
----------------------------------------

:Test ID: T-DCSC-013
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-013
:Implements: :ref:`Metric 9: Reused Dataset PID Resolves in the Repository <data.reused.feas.1>`

Description
^^^^^^^^^^^

Checks whether the persistent identifier declared in the maDMP resolves to an accessible online resource, confirming that the PID is active, valid, and leads to the correct dataset.

Input
^^^^^

- dataset_id from maDMP
- PID resolver

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Extract reused dataset identifiers from maDMP (`is_reused = true`).
2. Attempt resolution via the resolver (HTTP request).
3. Treat successful HTTP responses (2xx/3xx) as resolvable.
4. Pass if all PIDs resolve; otherwise fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-013",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check PID Resolves Successfully"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the persistent identifier declared in the maDMP resolves to an accessible online resource, confirming the PID is active and valid."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "persistent identifier"
          },
          {
            "@language": "en",
            "@value": "PID resolution"
          },
          {
            "@language": "en",
            "@value": "DOI"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.feas.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-14:

Test 14: Check Reused Data Access Matches Destination
-----------------------------------------------------

:Test ID: T-DCSC-014
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-014
:Implements: :ref:`Metric 10: Reused Dataset Access Conditions Match the Repository <data.reused.feas.2>`

Description
^^^^^^^^^^^

Check if reused data access in DMP matches the destination.

Input
^^^^^

- `data_access` in maDMP
- `access_right` in destination repository (e.g., Zenodo)

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Extract reused datasets from maDMP (`is_reused = true`).
2. For each reused dataset, retrieve its record from the destination repository.
3. Extract the repository access rights value.
4. Compare maDMP `data_access` with repository `access_right`.
5. Pass if all values match; otherwise fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-014",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check Reused Data Access Matches Destination"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Check if reused data access in DMP matches the destination."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "reused dataset"
          },
          {
            "@language": "en",
            "@value": "data access"
          },
          {
            "@language": "en",
            "@value": "repository"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.feas.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-15:

Test 15: Check Reused Data License Matches Destination
------------------------------------------------------

:Test ID: T-DCSC-015
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-015
:Implements: :ref:`Metric 11: Reused Dataset License Matches the Repository <data.reused.feas.3>`

Description
^^^^^^^^^^^

Checks if the license of the repository is the one mentioned in the DMP.

Input
^^^^^

- license in maDMP JSON
- license in destination repository (e.g., Zenodo)

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Extract reused datasets from maDMP (`is_reused = true`).
2. For each reused dataset, retrieve its record from the destination repository.
3. Extract the license value from the repository record.
4. Compare the repository license value with the maDMP license value.
5. Return pass if all values match; otherwise return fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-015",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check Reused Data License Matches Destination"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the license of the repository is the one mentioned in the DMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "reused dataset"
          },
          {
            "@language": "en",
            "@value": "data license"
          },
          {
            "@language": "en",
            "@value": "repository"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.reused.feas.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-16:

Test 16: Check for new data (no is_reused)
------------------------------------------

:Test ID: T-DCSC-016
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-016
:Implements: :ref:`Metric 12: New Dataset Declared in the DMP <data.new.1>`

Description
^^^^^^^^^^^

Checks whether the maDMP includes at least one dataset entry that does not carry an `is_reused` flag, confirming that newly produced or collected data is declared as part of the research project.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries (e.g., the `dataset` array).
3. Identify any dataset entry where the field `is_reused` is **absent**.
4. If at least one dataset without `is_reused` exists, return pass; otherwise return fail.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-016",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check for new data (no is_reused)"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the maDMP includes at least one dataset entry without an is_reused flag, confirming newly produced data is declared."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "new dataset"
          },
          {
            "@language": "en",
            "@value": "data production"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          },
          {
            "@language": "en",
            "@value": "completeness"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.new.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-17:

Test 17: Check technical_resource for new data collection/creation
------------------------------------------------------------------

:Test ID: T-DCSC-017
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-017
:Implements: :ref:`Metric 13: New Dataset Collection or Creation Method Declared <data.new.2>`

Description
^^^^^^^^^^^

Checks whether the `technical_resource` entries for new datasets include description, name, and identifier fields, confirming that the tools and methods used for data collection or creation are documented.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries.
3. Identify candidate “new” datasets according to your policy (e.g., datasets where `is_reused` is absent or not true).
4. For each candidate dataset, check whether `technical_resource` exists.
5. Verify that `technical_resource.description` and `technical_resource.name` exist and are non-empty.
6. Verify that `technical_resource.id.identifier` and `technical_resource.id.type` exist and are non-empty.
7. Return **pass** if at least one candidate “new” dataset satisfies all required fields; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-017",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check technical_resource for new data collection/creation"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the technical_resource entries for new datasets include description, name, and identifier fields documenting the data collection tools and methods."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "new dataset"
          },
          {
            "@language": "en",
            "@value": "technical resource"
          },
          {
            "@language": "en",
            "@value": "data collection"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.new.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-18:

Test 18: Check data_access for new datasets
-------------------------------------------

:Test ID: T-DCSC-018
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-018
:Implements: :ref:`Metric 14: New Dataset Has Declared Access Conditions <data.new.3>`

Description
^^^^^^^^^^^

Checks whether the `data_access` field for new datasets is declared with a recognised value — open, shared, or closed — confirming that access conditions for newly produced data are explicitly stated.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries.
3. Identify “new” datasets according to your policy (e.g., datasets where `is_reused` is absent or not true).
4. For each “new” dataset, check whether `data_access` exists.
5. Verify that `data_access` is one of: `open`, `shared`, `closed`.
6. Return **pass** if at least one “new” dataset has a valid `data_access`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-018",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check data_access for new datasets"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the data_access field for new datasets is declared with a recognised value — open, shared, or closed."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "new dataset"
          },
          {
            "@language": "en",
            "@value": "data access"
          },
          {
            "@language": "en",
            "@value": "access rights"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.new.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-19:

Test 19: Check rights of new dataset
------------------------------------

:Test ID: T-DCSC-019
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-019
:Implements: :ref:`Metric 14: New Dataset Has Declared Access Conditions <data.new.3>`

Description
^^^^^^^^^^^

Checks whether the `rights` field is present and non-empty for new datasets, confirming that the legal terms or conditions governing access to the newly produced data are documented.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries.
3. Identify “new” datasets according to your policy (e.g., datasets where `is_reused` is absent or not true).
4. For each “new” dataset, verify that a rights field/object exists (use your maDMP schema path, e.g., `rights`, `rights_statement`, or an equivalent rights block).
5. Verify the rights information is non-empty (e.g., contains a statement, URI, or controlled term).
6. Return **pass** if at least one “new” dataset contains rights information; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-019",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check rights of new dataset"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the rights field is present and non-empty for new datasets, confirming legal terms governing access are documented."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "new dataset"
          },
          {
            "@language": "en",
            "@value": "data rights"
          },
          {
            "@language": "en",
            "@value": "license"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.new.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-20:

Test 20: Check metadata for new dataset
---------------------------------------

:Test ID: T-DCSC-020
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-020
:Implements: :ref:`Metric 15: New Dataset Has Sufficient Metadata <data.new.4>`

Description
^^^^^^^^^^^

Checks whether new dataset entries include metadata fields such as description, language, and metadata standard identifier, confirming that sufficient information is provided for users to understand and reuse the data.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries.
3. Identify “new” datasets according to your policy (e.g., datasets where `is_reused` is absent or not true).
4. For each “new” dataset, verify that a `metadata` object exists.
5. Verify that `metadata.description` exists and is non-empty.
6. Verify that `metadata.language` exists and is non-empty.
7. Verify that `metadata.metadata_id.identifier` exists and is non-empty.
8. Verify that `metadata.metadata_id.type` exists and is non-empty.
9. Return **pass** if at least one “new” dataset satisfies all required metadata fields; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-020",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check metadata for new dataset"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether new dataset entries include metadata fields such as description, language, and metadata standard identifier."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "new dataset"
          },
          {
            "@language": "en",
            "@value": "metadata"
          },
          {
            "@language": "en",
            "@value": "reproducibility"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.new.4"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-21:

Test 21: Check dataset_id exists
--------------------------------

:Test ID: T-DCSC-021
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-021
:Implements: :ref:`Metric 16: New Dataset Persistent Identifier Resolves Successfully <data.new.feas.1>`

Description
^^^^^^^^^^^

Checks whether a `dataset_id` field with a non-empty identifier is present for the new dataset, confirming that the data has been assigned a reference that can be used to locate and cite it.

Input
^^^^^

dataset_id of maDMP

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries.
3. For each dataset, check whether `dataset_id` exists.
4. Return **pass** if at least one dataset includes `dataset_id`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-021",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check dataset_id exists"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether a dataset_id field with a non-empty identifier is present, confirming the new dataset has been assigned a referenceable identifier."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "new dataset"
          },
          {
            "@language": "en",
            "@value": "dataset identifier"
          },
          {
            "@language": "en",
            "@value": "PID"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.new.feas.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-22:

Test 22: Check PID resolves for dataset_id
------------------------------------------

:Test ID: T-DCSC-022
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-022
:Implements: :ref:`Metric 16: New Dataset Persistent Identifier Resolves Successfully <data.new.feas.1>`

Description
^^^^^^^^^^^

Checks whether the persistent identifier declared in the `dataset_id` field resolves successfully to an accessible online resource, confirming that the identifier is active and leads to the correct dataset record.

Input
^^^^^

dataset_id of maDMP in DOI resolver

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Extract all dataset identifiers from `dataset_id`.
3. For each identifier, attempt resolution using the appropriate resolver (e.g., HTTP request to a DOI resolver).
4. Treat successful HTTP responses (2xx/3xx) as resolvable.
5. Return **pass** if all tested PIDs resolve (or if your policy is “at least one resolves”, apply that consistently); otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-022",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check PID resolves for dataset_id"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the persistent identifier in the dataset_id field resolves successfully to an accessible online resource."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "persistent identifier"
          },
          {
            "@language": "en",
            "@value": "PID resolution"
          },
          {
            "@language": "en",
            "@value": "dataset identifier"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.new.feas.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-23:

Test 23: Check new data access matches destination
--------------------------------------------------

:Test ID: T-DCSC-023
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-023
:Implements: :ref:`Metric 17: New Dataset Access Conditions Match the Repository <data.new.feas.2>`

Description
^^^^^^^^^^^

Check if new data access in DMP matches the destination.

Input
^^^^^

data_access in maDMP + access_right in Zenodo

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Identify “new” datasets according to your policy (e.g., datasets where `is_reused` is absent or not true).
3. For each new dataset, extract `data_access`.
4. Query the destination repository (e.g., Zenodo) for the corresponding dataset record (using PID or repository identifier available in the maDMP).
5. Extract the repository’s `access_right` (or equivalent access-rights field).
6. Compare maDMP `data_access` with repository `access_right` using your project’s mapping rules (if value vocabularies differ, apply a normalization mapping).
7. Return **pass** if all compared datasets match; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-023",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check new data access matches destination"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Check if new data access in DMP matches the destination."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "new dataset"
          },
          {
            "@language": "en",
            "@value": "data access"
          },
          {
            "@language": "en",
            "@value": "repository"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.new.feas.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-24:

Test 24: Check new data license matches destination
---------------------------------------------------

:Test ID: T-DCSC-024
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-024
:Implements: :ref:`Metric 18: New Dataset License Matches the Repository <data.new.feas.3>`

Description
^^^^^^^^^^^

Checks if the license of the repository is the one mentioned in the DMP.

Input
^^^^^

license in maDMP JSON + license in Zenodo

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Identify “new” datasets according to your policy (e.g., datasets where `is_reused` is absent or not true).
3. For each new dataset, extract the maDMP license value (e.g., `license.ref` or equivalent field your schema uses).
4. Query the destination repository (e.g., Zenodo) for the corresponding dataset record (using PID or repository identifier available in the maDMP).
5. Extract the repository license value (e.g., Zenodo `license` field).
6. Normalize values if needed (e.g., map equivalent SPDX identifiers, URLs, or labels).
7. Compare the maDMP license value to the repository license value.
8. Return **pass** if all compared datasets match; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-024",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check new data license matches destination"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the license of the repository is the one mentioned in the DMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "new dataset"
          },
          {
            "@language": "en",
            "@value": "data license"
          },
          {
            "@language": "en",
            "@value": "repository"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.new.feas.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-25:

Test 25: Check dataset.type is specified
----------------------------------------

:Test ID: T-DCSC-025
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-025
:Implements: :ref:`Metric 19: Dataset Type Specified <data.info.cov.1>`

Description
^^^^^^^^^^^

Checks if the dataset type (e.g., qualitative or quantitative) is specified (`dataset.type`).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries (e.g., the `dataset` array).
3. For each dataset entry, check whether `dataset.type` exists and is non-empty.
4. If your project enforces a controlled vocabulary, verify the value is in the allowed set (e.g., `qualitative`, `quantitative`).
5. Return **pass** if all dataset entries in scope have a valid `dataset.type`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-025",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check dataset.type is specified"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the dataset type (e.g., qualitative or quantitative) is specified (`dataset.type`)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "dataset type"
          },
          {
            "@language": "en",
            "@value": "dataset classification"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          },
          {
            "@language": "en",
            "@value": "coverage"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.info.cov.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-26:

Test 26: Check distribution.format is specified
-----------------------------------------------

:Test ID: T-DCSC-026
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-026
:Implements: :ref:`Metric 20: Dataset File Format Specified <data.info.cov.2>`

Description
^^^^^^^^^^^

Checks whether the `format` field within the dataset distribution entry is present and non-empty, confirming that the file format of the data has been declared so users know what tools are needed to open it.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their `distribution` objects/arrays.
3. For each distribution in scope, check whether `distribution.format` exists and is non-empty.
4. If your project enforces a controlled vocabulary (e.g., MIME types), optionally validate the value against that vocabulary.
5. Return **pass** if all distributions in scope have a non-empty `distribution.format`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-026",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check distribution.format is specified"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the format field within the dataset distribution entry is present and non-empty, confirming the file format has been declared."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "file format"
          },
          {
            "@language": "en",
            "@value": "distribution"
          },
          {
            "@language": "en",
            "@value": "interoperability"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.info.cov.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-27:

Test 27: Check distribution.byte_size is specified
--------------------------------------------------

:Test ID: T-DCSC-027
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-027
:Implements: :ref:`Metric 21: Dataset Size Specified <data.info.cov.3>`

Description
^^^^^^^^^^^

Checks whether the `byte_size` field within the dataset distribution entry is present and has a positive value, confirming that the size of the dataset has been declared to support storage planning.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their `distribution` objects/arrays.
3. For each distribution in scope, check whether `distribution.byte_size` exists.
4. Verify that `distribution.byte_size` is numeric (integer or float) and is **≥ 0**.
5. Return **pass** if all distributions in scope have a valid non-negative `distribution.byte_size`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-027",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check distribution.byte_size is specified"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the byte_size field within the distribution entry is present and has a positive value, confirming the dataset size has been declared."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "dataset size"
          },
          {
            "@language": "en",
            "@value": "storage planning"
          },
          {
            "@language": "en",
            "@value": "distribution"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.info.cov.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-28:

Test 28: Check dataset.type matches destination type
----------------------------------------------------

:Test ID: T-DCSC-028
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-028
:Implements: :ref:`Metric 22: Dataset Type Matches the Repository <data.info.feas.1>`

Description
^^^^^^^^^^^

Checks that dataset is both the type of each destination.

Input
^^^^^

dataset.type in maDMP + type in Zenodo

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. For each dataset in scope, extract `dataset.type`.
3. Determine the destination repository record corresponding to the dataset (e.g., via dataset PID/identifier in the maDMP).
4. Query the destination repository (e.g., Zenodo API/metadata endpoint) and retrieve the record `type`.
5. Normalize values if needed (e.g., mapping maDMP vocabulary to Zenodo vocabulary).
6. Compare maDMP `dataset.type` with destination `type`.
7. Return **pass** if all compared datasets match; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-028",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check dataset.type matches destination type"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that dataset is both the type of each destination."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "dataset type"
          },
          {
            "@language": "en",
            "@value": "repository"
          },
          {
            "@language": "en",
            "@value": "type consistency"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.info.feas.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-29:

Test 29: Check dataset.type aligns with destination subtype
-----------------------------------------------------------

:Test ID: T-DCSC-029
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-029
:Implements: :ref:`Metric 22: Dataset Type Matches the Repository <data.info.feas.1>`

Description
^^^^^^^^^^^

Checks whether the dataset type declared in the maDMP aligns with the sub-type or resource type classification used by the destination repository, confirming consistency in how the data is categorised.

Input
^^^^^

dataset.type in maDMP + subtype in Zenodo

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. For each dataset in scope, extract `dataset.type` (and any local sub-property if your maDMP schema includes it).
3. Retrieve the corresponding destination record from the repository (e.g., Zenodo).
4. Extract destination `subtype` (or equivalent sub-classification field).
5. Apply a mapping/normalization rule that relates maDMP `dataset.type` to acceptable destination subtypes (because subtype may be more granular than type).
6. Verify that the destination subtype is compatible with the maDMP dataset type (or that the maDMP type can be inferred from the subtype).
7. Return **pass** if all compared datasets are compatible; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-029",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check dataset.type aligns with destination subtype"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether the dataset type declared in the maDMP aligns with the sub-type or resource type classification used by the destination repository."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "dataset type"
          },
          {
            "@language": "en",
            "@value": "repository"
          },
          {
            "@language": "en",
            "@value": "subtype"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.info.feas.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-30:

Test 30: Check final dataset format matches destination files
-------------------------------------------------------------

:Test ID: T-DCSC-030
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-030
:Implements: :ref:`Metric 23: Dataset File Format Matches the Repository <data.info.feas.2>`

Description
^^^^^^^^^^^

Checks whether the file format declared in the maDMP for the dataset distribution matches the actual file format of the data deposited in the destination repository, confirming that the plan reflects reality.

Input
^^^^^

distribution.format in maDMP + files in Zenodo

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset distributions in scope and extract `distribution.format`.
3. Identify the corresponding destination repository record (e.g., Zenodo) for the dataset/distribution using a PID or repository identifier available in the maDMP.
4. Query the destination repository and retrieve the list of deposited files and their format information (e.g., filename extensions and/or MIME types if provided).
5. Normalize formats for comparison (e.g., map extensions to MIME types, normalize case, apply a controlled vocabulary or mapping table).
6. Compare maDMP `distribution.format` to the observed destination file format(s): - **Strict mode:** every maDMP format must be present among destination formats. - **Compatible mode:** maDMP format is considered valid if it maps to at least one destination file format under your mapping table.
7. Return **pass** if the comparison succeeds for all distributions in scope; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-030",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check final dataset format matches destination files"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether final dataset format matches destination files as required by the maDMP specification."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "file format"
          },
          {
            "@language": "en",
            "@value": "repository"
          },
          {
            "@language": "en",
            "@value": "format consistency"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.info.feas.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-31:

Test 31: Check final dataset size matches destination size
----------------------------------------------------------

:Test ID: T-DCSC-031
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-031
:Implements: :ref:`Metric 24: Dataset Size Matches the Repository <data.info.feas.3>`

Description
^^^^^^^^^^^

Checks whether the dataset size declared in the maDMP matches the actual size of the data deposited in the destination repository, confirming that the stated and actual storage requirements are consistent.

Input
^^^^^

distribution.byte_size in maDMP + size in Zenodo

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset distributions in scope and extract `distribution.byte_size`.
3. Identify the corresponding destination repository record (e.g., Zenodo) using a PID or repository identifier available in the maDMP.
4. Query the destination repository and retrieve the deposited size value: - If Zenodo provides per-file sizes, compute a total size (sum of file sizes) for the record, or compare per distribution if your mapping supports it.
5. Normalize size units (ensure all sizes are compared in bytes).
6. Compare maDMP `distribution.byte_size` to destination size: - **Exact mode:** values must be equal. - **Tolerance mode (optional):** values must be within an acceptable difference threshold (define e.g., ±1%).
7. Return **pass** if all distributions in scope match (per chosen mode); otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-031",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check final dataset size matches destination size"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether final dataset size matches destination size as required by the maDMP specification."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "dataset size"
          },
          {
            "@language": "en",
            "@value": "repository"
          },
          {
            "@language": "en",
            "@value": "size consistency"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.info.feas.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-32:

Test 32: Check maDMP JSON Validates Against DMP Common Standard Schema
----------------------------------------------------------------------

:Test ID: T-DCSC-032
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-032
:Implements: :ref:`Metric 25: DMP Common Standard Field Compliance <meta.comp.1>`

Description
^^^^^^^^^^^

Checks if the JSON matches with DMP Common Standard schema.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Obtain the DMP Common Standard JSON Schema version used by your project (local file or URL).
2. Load/parse the input maDMP JSON document.
3. Run JSON Schema validation of the maDMP against the DMP Common Standard schema.
4. If validation reports **zero** errors, return **pass**.
5. If one or more validation errors are reported, return **fail** and record the validation error details (path, expected type, etc.) as diagnostic output.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-032",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check maDMP JSON Validates Against DMP Common Standard Schema"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the JSON matches with DMP Common Standard schema."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "DMP Common Standard"
          },
          {
            "@language": "en",
            "@value": "schema validation"
          },
          {
            "@language": "en",
            "@value": "JSON"
          },
          {
            "@language": "en",
            "@value": "compliance"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/meta.comp.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-33:

Test 33: Check dataset_methodology for controlled vocabularies
--------------------------------------------------------------

:Test ID: T-DCSC-033
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-033
:Implements: :ref:`Metric 26: Controlled Vocabularies Used in Methodology <meta.co.1>`

Description
^^^^^^^^^^^

Checks whether the methodology description in the maDMP references terms from a recognised controlled vocabulary, confirming that the research methods are described in a standardised and interoperable way.

Input
^^^^^

maDMP JSON + controlled vocabularies from external sources

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset methodology information (e.g., `dataset_methodology` or the equivalent field in your schema).
3. Extract methodology terms, identifiers, URIs, or references used in that field.
4. Compare the extracted values against recognized controlled vocabularies or ontology sources defined by your project or external reference lists.
5. Verify whether at least one methodology element points to, or can be matched with, a controlled vocabulary term or external vocabulary source.
6. Return **pass** if controlled vocabulary usage is detected in methodology; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-033",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check dataset_methodology for controlled vocabularies"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether dataset_methodology for controlled vocabularies as required by the maDMP specification."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "controlled vocabulary"
          },
          {
            "@language": "en",
            "@value": "methodology"
          },
          {
            "@language": "en",
            "@value": "interoperability"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/meta.co.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-34:

Test 34: Check technical_resource.name for electronic lab notebook reference
----------------------------------------------------------------------------

:Test ID: T-DCSC-034
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-034
:Implements: :ref:`Metric 31: Electronic Lab Notebook Referenced as a Technical Resource <meta.doc.qual.1>`

Description
^^^^^^^^^^^

Checks whether the `technical_resource.name` field in the maDMP includes a reference to an electronic lab notebook, confirming that the use of this documentation tool has been declared in the plan.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `technical_resource` entries in scope.
3. Extract each `technical_resource.name` value.
4. Check whether any name explicitly mentions an electronic lab notebook or a known ELN tool/service name used by your project.
5. Return **pass** if at least one technical resource name indicates an ELN; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-034",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check technical_resource.name for electronic lab notebook reference"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if an electronic lab notebook is mentioned (`technical_resource.name`)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "electronic lab notebook"
          },
          {
            "@language": "en",
            "@value": "ELN"
          },
          {
            "@language": "en",
            "@value": "technical resource"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/meta.doc.qual.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-35:

Test 35: Check related_identifier resource_type for ReadMe file
---------------------------------------------------------------

:Test ID: T-DCSC-035
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-035
:Implements: :ref:`Metric 28: ReadMe File Reference <meta.qual.2>`

Description
^^^^^^^^^^^

Checks if a ReadMe file is included in the related_identifier resource_type.

Input
^^^^^

json madmp

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `related_identifier` entries in scope.
3. Extract the `resource_type` (or equivalent field) for each related identifier.
4. Check whether any `resource_type` value indicates a ReadMe file (for example `ReadMe`, `README`, or a project-defined equivalent).
5. Return **pass** if at least one related identifier references a ReadMe file; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-035",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check related_identifier resource_type for ReadMe file"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if a ReadMe file is included in the related_identifier resource_type."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "template keyword"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/meta.qual.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-36:

Test 36: Check metadata_standard_id is registered in metadata registries
------------------------------------------------------------------------

:Test ID: T-DCSC-036
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-036
:Implements: :ref:`Metric 29: Metadata Standards Used <meta.stand.comp.1>`

Description
^^^^^^^^^^^

Checks metadata_standard_id to be registered in RDA Directory and FAIRsharing.

Input
^^^^^

metadata in maDMP + metadata registries (https://rdamsc.bath.ac.uk/)

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate metadata standard identifiers in scope (e.g., `metadata_standard_id` or equivalent schema field).
3. Extract the metadata standard identifiers or names.
4. Check whether each extracted metadata standard can be matched against recognized metadata registries such as the RDA Metadata Standards Catalog and FAIRsharing.
5. If your project uses identifier normalization, normalize names, URIs, or registry identifiers before comparison.
6. Return **pass** if all metadata standards in scope are found in the registries; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-036",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check metadata_standard_id is registered in metadata registries"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks metadata_standard_id to be registered in RDA Directory and FAIRsharing."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "template keyword"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/meta.stand.comp.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-37:

Test 37: Check distribution format is open
------------------------------------------

:Test ID: T-DCSC-037
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-037
:Implements: :ref:`Metric 30: Dataset Distributions Use Open File Formats <meta.form.op.1>`

Description
^^^^^^^^^^^

Checks distribution_format to be open.

Input
^^^^^

madmp

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset distributions in scope and extract the declared format field (e.g., `distribution_format` or the equivalent schema field such as `distribution.format`).
3. Normalize the extracted format values if needed (e.g., extension, MIME type, or controlled term).
4. Compare each format against the list, registry, or rule set your project uses to classify formats as open.
5. Return **pass** if all formats in scope are classified as open; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-037",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check distribution format is open"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks distribution_format to be open."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "template keyword"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/meta.form.op.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-38:

Test 38: Check ELN dataset linked via related_ids
-------------------------------------------------

:Test ID: T-DCSC-038
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-038
:Implements: :ref:`Metric 31: Electronic Lab Notebook Linked <meta.doc.qual.1>`

Description
^^^^^^^^^^^

Checks that the electronic lab notebook dataset or `technical_resource.name` includes `related_ids` with the dataset.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `technical_resource` objects.
3. For each `technical_resource`, check whether `technical_resource.name` identifies an electronic lab notebook.
4. If an ELN technical resource is found, verify that `related_ids` (or equivalent related identifier field) is present and contains at least one entry linking back to the dataset.
5. Additionally, check the dataset's `related_identifier` entries for any reference that identifies an ELN record.
6. Return **pass** if at least one dataset has a confirmed ELN linkage via `related_ids` or `related_identifier`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-038",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check ELN dataset linked via related_ids"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that the electronic lab notebook dataset or technical_resource.name includes related_ids with the dataset."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "electronic lab notebook"
          },
          {
            "@language": "en",
            "@value": "related identifier"
          },
          {
            "@language": "en",
            "@value": "dataset linkage"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/meta.doc.qual.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-39:

Test 39: Check technical_resource for dataset documentation
-----------------------------------------------------------

:Test ID: T-DCSC-039
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-039
:Implements: :ref:`Metric 32: Existence of Dataset Documentation <meta.feas.1>`

Description
^^^^^^^^^^^

Checks if there is the presence of any documentation supporting the dataset.

Input
^^^^^

`technical_resource.name`; `technical_resource.technical_resource_id` in maDMP

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `technical_resource` objects or arrays.
3. For each `technical_resource` entry, check whether `technical_resource.name` exists and is non-empty.
4. Additionally check whether `technical_resource.technical_resource_id` exists and is non-empty.
5. Return **pass** if at least one dataset contains a `technical_resource` entry with a non-empty `name` or `technical_resource_id`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-039",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check technical_resource for dataset documentation"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if there is the presence of any documentation supporting the dataset."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "dataset documentation"
          },
          {
            "@language": "en",
            "@value": "technical resource"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/meta.feas.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-40:

Test 40: Check data_quality_assurance for quality control methods
-----------------------------------------------------------------

:Test ID: T-DCSC-040
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-040
:Implements: :ref:`Metric 33: Quality Control Methods Stated <qc.qual.1>`

Description
^^^^^^^^^^^

Checks if quality control methods are mentioned, either as narrative or controlled terms (`data_quality_assurance`).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries in scope.
3. For each dataset, check whether the `data_quality_assurance` field exists.
4. Verify that the field is non-empty — either containing a free-text narrative description or one or more controlled terms.
5. Return **pass** if at least one dataset contains a non-empty `data_quality_assurance` value; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-040",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check data_quality_assurance for quality control methods"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if quality control methods are mentioned, either as narrative or controlled terms (data_quality_assurance)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "quality control"
          },
          {
            "@language": "en",
            "@value": "data quality assurance"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          },
          {
            "@language": "en",
            "@value": "quality"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/qc.qual.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-41:

Test 41: Check host.title and host.url for storage location
-----------------------------------------------------------

:Test ID: T-DCSC-041
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-041
:Implements: :ref:`Metric 34: Data Storage Location mentioned in the DMP <store.cov.1>`

Description
^^^^^^^^^^^

Checks if there is a reference of storage (`host.title`; `host.url`).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `host` object is present.
4. Verify that `host.title` exists and is non-empty, or that `host.url` exists and is non-empty.
5. Return **pass** if at least one distribution contains a `host` entry with a non-empty `title` or `url`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-041",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check host.title and host.url for storage location"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if there is a reference of storage (host.title; host.url)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "data storage"
          },
          {
            "@language": "en",
            "@value": "storage location"
          },
          {
            "@language": "en",
            "@value": "host"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/store.cov.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-42:

Test 42: Check host for trusted repository storage
--------------------------------------------------

:Test ID: T-DCSC-042
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-042
:Implements: :ref:`Metric 35: Use of Secure Storage for the dataset in a trusted repository <store.cov.2>`

Description
^^^^^^^^^^^

Checks if the data are stored in trusted repositories (`host`).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `host` object is present.
4. Inspect `host` properties (e.g., `host.title`, `host.url`, `host.certified_with`, `host.pid_system`) to determine whether the declared host can be identified as a trusted or institutional repository.
5. Apply your project's rule set for classifying a host as trusted (e.g., presence of a certification, match against a known repository list, or absence of indicators of personal storage).
6. Return **pass** if at least one distribution declares a host that qualifies as a trusted repository; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-042",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check host for trusted repository storage"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the data are stored in trusted repositories (host)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "trusted repository"
          },
          {
            "@language": "en",
            "@value": "secure storage"
          },
          {
            "@language": "en",
            "@value": "host"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/store.cov.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-43:

Test 43: Check sensitive_data classification is assigned
--------------------------------------------------------

:Test ID: T-DCSC-043
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-043
:Implements: :ref:`Metric 36: Alignment of Storage and Backup with Information Sensitivity <store.comp.1>`

Description
^^^^^^^^^^^

Checks if the dataset has an assigned classification level (`sensitive_data`).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries in scope.
3. For each dataset, check whether the `sensitive_data` field is present.
4. Verify that the value is explicit and valid (e.g., a boolean or controlled term allowed by your schema).
5. Return **pass** if at least one dataset contains an explicitly set `sensitive_data` value; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-043",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check sensitive_data classification is assigned"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the dataset has an assigned classification level (sensitive_data)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "sensitive data"
          },
          {
            "@language": "en",
            "@value": "data classification"
          },
          {
            "@language": "en",
            "@value": "compliance"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/store.comp.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-44:

Test 44: Check host security and backup reflect sensitivity level
-----------------------------------------------------------------

:Test ID: T-DCSC-044
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-044
:Implements: :ref:`Metric 36: Alignment of Storage and Backup with Information Sensitivity <store.comp.1>`

Description
^^^^^^^^^^^

Checks if the host/storage method reflects appropriate protection level (`security_and_privacy`; `backup_type`).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `host` object is present.
4. Verify that `host.security_and_privacy` exists and is non-empty.
5. Verify that `host.backup_type` exists and is non-empty.
6. Cross-reference the declared `sensitive_data` value for the dataset with the `security_and_privacy` and `backup_type` values, applying your project's mapping rules for appropriate protection levels.
7. Return **pass** if at least one distribution declares storage and backup properties consistent with the dataset's sensitivity classification; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-044",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check host security and backup reflect sensitivity level"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the host/storage method reflects appropriate protection level (security_and_privacy; backup_type)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "storage security"
          },
          {
            "@language": "en",
            "@value": "backup"
          },
          {
            "@language": "en",
            "@value": "sensitive data"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/store.comp.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-45:

Test 45: Check contributor.role for backup responsibility
---------------------------------------------------------

:Test ID: T-DCSC-045
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-045
:Implements: :ref:`Metric 37: Back up Responsibility <store.cov.3>`

Description
^^^^^^^^^^^

Checks if someone is responsible for back up activities (`contributor.role`).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `contributor` entries in scope (at DMP level or dataset level, depending on your schema).
3. For each contributor, extract the `role` field value.
4. Check whether any `role` value indicates backup responsibility according to your project's controlled vocabulary or role list (e.g., a backup manager, data steward, or equivalent term).
5. Return **pass** if at least one contributor has a role associated with backup responsibility; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-045",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check contributor.role for backup responsibility"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if someone is responsible for back up activities (contributor.role)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "backup responsibility"
          },
          {
            "@language": "en",
            "@value": "contributor role"
          },
          {
            "@language": "en",
            "@value": "data stewardship"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/store.cov.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-46:

Test 46: Check backup_frequency is declared
-------------------------------------------

:Test ID: T-DCSC-046
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-046
:Implements: :ref:`Metric 38: Back up Frequency <store.co.1>`

Description
^^^^^^^^^^^

Checks whether the `backup_frequency` field in the maDMP is present and non-empty, confirming that the plan specifies how often data backups will be performed to protect against loss.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `host` object is present.
4. Verify that `host.backup_frequency` exists and is non-empty.
5. Return **pass** if at least one distribution declares a non-empty `backup_frequency`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-046",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check backup_frequency is declared"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the back up performance is frequent (backup_frequency)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "backup frequency"
          },
          {
            "@language": "en",
            "@value": "backup schedule"
          },
          {
            "@language": "en",
            "@value": "data storage"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/store.co.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-47:

Test 47: Check host.id matches Zenodo deposit location
------------------------------------------------------

:Test ID: T-DCSC-047
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-047
:Implements: :ref:`Metric 40: Stored Dataset Location Confirmed <stor.feas.1>`

Description
^^^^^^^^^^^

Checks if the storage of the data matches the destination.

Input
^^^^^

`host.id` in maDMP + id in Zenodo

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, extract the `host.id` value.
4. Query the target repository (e.g., Zenodo API) using the dataset identifier to retrieve the actual deposit record.
5. Compare the `host.id` from the maDMP with the repository identifier returned by the external query.
6. Return **pass** if the `host.id` resolves and matches the confirmed deposit location in the target repository; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-047",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check host.id matches Zenodo deposit location"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the storage of the data matches the destination."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "storage location"
          },
          {
            "@language": "en",
            "@value": "deposit confirmation"
          },
          {
            "@language": "en",
            "@value": "Zenodo"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/stor.feas.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-48:

Test 48: Check security_and_privacy.title for security measures
---------------------------------------------------------------

:Test ID: T-DCSC-048
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-048
:Implements: :ref:`Metric 41: Security Measures Implementation <secur.co.1>`

Description
^^^^^^^^^^^

Checks whether the `security_and_privacy.title` field is present and non-empty in the maDMP, confirming that at least one security measure has been named and associated with the dataset.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `host` object containing a `security_and_privacy` array or object is present.
4. For each `security_and_privacy` entry, verify that `title` exists and is non-empty.
5. Return **pass** if at least one distribution contains a `security_and_privacy` entry with a non-empty `title`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-048",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check security_and_privacy.title for security measures"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks whether security_and_privacy.title for security measures as required by the maDMP specification."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "security measures"
          },
          {
            "@language": "en",
            "@value": "data security"
          },
          {
            "@language": "en",
            "@value": "security and privacy"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/secur.co.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-49:

Test 49: Check security_and_privacy.description for access rights management
----------------------------------------------------------------------------

:Test ID: T-DCSC-049
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-049
:Implements: :ref:`Metric 42: Sensitive Data Protection Description <secur.co.2>`

Description
^^^^^^^^^^^

Checks if the sensitive data includes a description for access rights management (`security_and_privacy.description`).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and identify those where `sensitive_data` is set to true or an equivalent positive value.
3. For each sensitive dataset, locate the associated `distribution` objects and their `host` entries.
4. Check whether a `security_and_privacy` object or array is present within the host.
5. For each `security_and_privacy` entry, verify that `description` exists, is non-empty, and contains a reference to access rights management (e.g., institutional storage, access controls, or authorization mechanisms).
6. Return **pass** if at least one sensitive dataset has a qualifying `security_and_privacy.description`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-049",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check security_and_privacy.description for access rights management"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the sensitive data includes a description for access rights management (security_and_privacy.description)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "sensitive data"
          },
          {
            "@language": "en",
            "@value": "access rights management"
          },
          {
            "@language": "en",
            "@value": "data protection"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/secur.co.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-50:

Test 50: Check security_and_privacy.description for authorised access controls
------------------------------------------------------------------------------

:Test ID: T-DCSC-050
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-050
:Implements: :ref:`Metric 43: Authorised Access Control <secur.co.3>`

Description
^^^^^^^^^^^

Checks if access control measures exist for authorised users (`security_and_privacy.description`).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `host` object containing a `security_and_privacy` array or object is present.
4. For each `security_and_privacy` entry, verify that `description` exists and is non-empty.
5. Check whether the `description` value contains a reference to access control measures for authorised users (e.g., role-based access, authentication, user authorisation procedures, or equivalent terms defined by your project's vocabulary).
6. Return **pass** if at least one qualifying `security_and_privacy.description` is found; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-050",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check security_and_privacy.description for authorised access controls"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if access control measures exist for authorised users (security_and_privacy.description)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "access control"
          },
          {
            "@language": "en",
            "@value": "authorised users"
          },
          {
            "@language": "en",
            "@value": "data security"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/secur.co.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-51:

Test 51: Check security_and_privacy.description for access control and user permissions
---------------------------------------------------------------------------------------

:Test ID: T-DCSC-051
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-051
:Implements: :ref:`Metric 44: Access Control and User Management <secur.co.4>`

Description
^^^^^^^^^^^

Checks how access to the data is controlled and if user roles or permissions are defined (`security_and_privacy.description`).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and identify those where sensitive data is present.
3. For each such dataset, locate the associated `distribution` objects and their `host` entries.
4. Check whether a `security_and_privacy` object or array is present within each host.
5. For each `security_and_privacy` entry, verify that `description` exists and is non-empty.
6. Check whether the `description` references both access control mechanisms and user roles or permissions (e.g., role-based access control, permission levels, user group definitions, or equivalent terms defined by your project's vocabulary).
7. Return **pass** if at least one qualifying `security_and_privacy.description` is found; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-051",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check security_and_privacy.description for access control and user permissions"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks how access to the data is controlled and if user roles or permissions are defined (security_and_privacy.description)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "access control"
          },
          {
            "@language": "en",
            "@value": "user management"
          },
          {
            "@language": "en",
            "@value": "user permissions"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/secur.co.4"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-52:

Test 52: Check security_and_privacy.description for access procedures
---------------------------------------------------------------------

:Test ID: T-DCSC-052
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-052
:Implements: :ref:`Metric 45: Required Access Procedures <secur.co.5>`

Description
^^^^^^^^^^^

Checks if access procedures for restricted/sensitive data are described in the DMP (`security_and_privacy.description`).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `host` object containing a `security_and_privacy` array or object is present.
4. For each `security_and_privacy` entry, verify that `description` exists and is non-empty.
5. Check whether the `description` contains a reference to access procedures for restricted or sensitive data (e.g., a data access request process, approval workflow, designated contact point for access, or equivalent procedural terms defined by your project's vocabulary).
6. Return **pass** if at least one qualifying `security_and_privacy.description` is found; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-052",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check security_and_privacy.description for access procedures"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if access procedures for restricted/sensitive data are described in the DMP (security_and_privacy.description)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "access procedures"
          },
          {
            "@language": "en",
            "@value": "restricted data"
          },
          {
            "@language": "en",
            "@value": "data access request"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/secur.co.5"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-53:

Test 53: Check security_and_privacy.description and ethical_issues_report for GDPR and ethics compliance
--------------------------------------------------------------------------------------------------------

:Test ID: T-DCSC-053
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-053
:Implements: :ref:`Metric 46: GDPR and Ethics Compliance <secur.comp.1>`

Description
^^^^^^^^^^^

Checks if GDPR and ethical review is mentioned in the DMP `security_and_privacy.description` of the maDMP, validated against the GDPR checklist at https://gdpr.eu/checklist/, and whether `ethical_issues_report` is present.

Input
^^^^^

`security_and_privacy.description` in maDMP JSON; `ethical_issues_report` in maDMP JSON; GDPR checklist at https://gdpr.eu/checklist/

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `host` object containing a `security_and_privacy` array or object is present.
4. For each `security_and_privacy` entry, verify that `description` exists and is non-empty, and check whether it contains a reference to GDPR or applicable data protection legislation (cross-validated against the GDPR checklist at https://gdpr.eu/checklist/).
5. Independently, check whether the maDMP includes an `ethical_issues_report` field that is present and non-empty.
6. Return **pass** if at least one of the following conditions is met: a qualifying `security_and_privacy.description` referencing GDPR is found, or a non-empty `ethical_issues_report` is present; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-053",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check security_and_privacy.description and ethical_issues_report for GDPR and ethics compliance"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if GDPR and ethical review is mentioned in the DMP security_and_privacy.description of the maDMP, validated against the GDPR checklist, and whether ethical_issues_report is present."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "GDPR"
          },
          {
            "@language": "en",
            "@value": "ethics compliance"
          },
          {
            "@language": "en",
            "@value": "ethical review"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/secur.comp.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-54:

Test 54: Check security_and_privacy.title for implemented security measures at destination
------------------------------------------------------------------------------------------

:Test ID: T-DCSC-054
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-054
:Implements: :ref:`Metric 47: Final Security Measures Implementation <secur.feas.1>`

Description
^^^^^^^^^^^

Checks if security measures are implemented in the destination (`security_and_privacy.title` in maDMP).

Input
^^^^^

`security_and_privacy.title` in maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `host` object containing a `security_and_privacy` array or object is present.
4. For each `security_and_privacy` entry, verify that `title` exists and is non-empty.
5. Return **pass** if at least one distribution contains a `security_and_privacy` entry with a non-empty `title`, confirming that a security measure is implemented at the destination; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-054",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check security_and_privacy.title for implemented security measures at destination"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if security measures are implemented in the destination (security_and_privacy.title in maDMP)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "security measures"
          },
          {
            "@language": "en",
            "@value": "destination repository"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/secur.feas.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-55:

Test 55: Check security_and_privacy.description for data protection method when sensitive_data is true
------------------------------------------------------------------------------------------------------

:Test ID: T-DCSC-055
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-055
:Implements: :ref:`Metric 48: Sensitive Data Using Method <sens.secure.co.1>`

Description
^^^^^^^^^^^

Checks if a data protection method is mentioned when sensitive data exist.

Input
^^^^^

maDMP JSON — if `sensitive_data` = yes, then check `security_and_privacy.description`

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and identify those where `sensitive_data` is set to true or an equivalent positive value.
3. If no dataset is flagged as sensitive, return **pass** (metric is not applicable).
4. For each sensitive dataset, locate the associated `distribution` objects and their `host` entries.
5. Check whether a `security_and_privacy` object or array is present within each host.
6. For each `security_and_privacy` entry, verify that `description` exists, is non-empty, and describes a method used to protect the sensitive data.
7. Return **pass** if at least one sensitive dataset has a qualifying `security_and_privacy.description`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-055",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check security_and_privacy.description for data protection method when sensitive_data is true"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if a data protection method is mentioned when sensitive data exist."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "sensitive data"
          },
          {
            "@language": "en",
            "@value": "data protection method"
          },
          {
            "@language": "en",
            "@value": "security and privacy"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/sens.secure.co.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-56:

Test 56: Check security_and_privacy for anonymised synthetic data provision
---------------------------------------------------------------------------

:Test ID: T-DCSC-056
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-056
:Implements: :ref:`Metric 49: Provision of Anonymised Synthetic Data <sens.secure.co.2>`

Description
^^^^^^^^^^^

Checks if anonymised synthetic data will be provided (`security_and_privacy` in maDMP).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `host` object containing a `security_and_privacy` array or object is present.
4. For each `security_and_privacy` entry, inspect both `title` and `description` fields for references to anonymisation, pseudonymisation, synthetic data generation, or equivalent terms indicating the intent to provide an anonymised or synthetic version of the data.
5. Return **pass** if at least one qualifying `security_and_privacy` entry is found; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-056",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check security_and_privacy for anonymised synthetic data provision"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if anonymised synthetic data will be provided (security_and_privacy in maDMP)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "anonymisation"
          },
          {
            "@language": "en",
            "@value": "synthetic data"
          },
          {
            "@language": "en",
            "@value": "sensitive data"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/sens.secure.co.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-57:

Test 57: Check rights for statement of no data restrictions
-----------------------------------------------------------

:Test ID: T-DCSC-057
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-057
:Implements: :ref:`Metric 50: Statement of No Data Restrictions <data.restrict.co.3>`

Description
^^^^^^^^^^^

Checks if there are any restrictions applied to the data (`rights` in maDMP).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `rights` field (or equivalent access rights field) is present.
4. Inspect the `rights` value to determine whether it explicitly indicates that no restrictions apply (e.g., an open licence URI, a public domain declaration, or a value such as "open" or "unrestricted" as defined by your project's controlled vocabulary).
5. Return **pass** if at least one distribution contains a `rights` value that confirms the absence of restrictions; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-057",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check rights for statement of no data restrictions"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if there are any restrictions applied to the data (rights in maDMP)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "data restrictions"
          },
          {
            "@language": "en",
            "@value": "access rights"
          },
          {
            "@language": "en",
            "@value": "open access"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.restrict.co.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-58:

Test 58: Check license_ref for dataset licence
----------------------------------------------

:Test ID: T-DCSC-058
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-058
:Implements: :ref:`Metric 51: Dataset License Declared <data.lice.co.1>`

Description
^^^^^^^^^^^

Checks whether the `license_ref` field within the dataset distribution entry is present and non-empty, confirming that a license has been declared and users know the terms under which the data may be used.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `license_ref` field is present.
4. Verify that the `license_ref` value is non-empty and resolves to a recognisable licence identifier or URI.
5. Return **pass** if at least one distribution contains a non-empty `license_ref`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-058",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check license_ref for dataset licence"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the dataset has a licence (license_ref)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "dataset licence"
          },
          {
            "@language": "en",
            "@value": "license reference"
          },
          {
            "@language": "en",
            "@value": "open licence"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.lice.co.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-59:

Test 59: Check license_ref against SPDX for software datasets
-------------------------------------------------------------

:Test ID: T-DCSC-059
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-059
:Implements: :ref:`Metric 52: Software Dataset Has a Standardised Machine-Readable License <soft.lice.comp.1>`

Description
^^^^^^^^^^^

Checks if the dataset type is software, then verifies that `license_ref` matches a recognised software licence from the SPDX licence list at https://spdx.org/licenses/.

Input
^^^^^

maDMP JSON; SPDX licence list at https://spdx.org/licenses/

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and identify those where `type` is set to software or an equivalent value.
3. If no dataset is typed as software, return **pass** (metric is not applicable).
4. For each software dataset, locate the associated `distribution` objects and check whether a `license_ref` field is present and non-empty.
5. Retrieve the current SPDX licence list from https://spdx.org/licenses/ and check whether the declared `license_ref` value matches a recognised SPDX licence identifier or URI.
6. Return **pass** if at least one software dataset declares a `license_ref` that matches a recognised SPDX software licence; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-059",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check license_ref against SPDX for software datasets"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the dataset type is software, then verifies that license_ref matches a recognised software licence from the SPDX licence list."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "software licence"
          },
          {
            "@language": "en",
            "@value": "SPDX"
          },
          {
            "@language": "en",
            "@value": "licence compliance"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/soft.lice.comp.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-60:

Test 60: Check data_access and rights for access agreements or MoUs
-------------------------------------------------------------------

:Test ID: T-DCSC-060
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-060
:Implements: :ref:`Metric 53: Data Access Agreements <data.agree.comp.2>`

Description
^^^^^^^^^^^

Checks the `data_access` and `rights` fields in the maDMP for references to collaborative agreements or MoUs.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries in scope.
3. For each dataset, check whether a `data_access` field is present and inspect its value for references to a formal data access agreement or MoU.
4. Additionally, locate associated `distribution` objects and check whether `rights` entries reference a formal agreement or MoU (e.g., a named agreement, a URI pointing to an agreement document, or explicit mention of collaborative access terms).
5. Return **pass** if at least one dataset contains a qualifying reference to a data access agreement or MoU in either `data_access` or `rights`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-060",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check data_access and rights for access agreements or MoUs"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks the data_access and rights fields in the maDMP for references to collaborative agreements or MoUs."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "data access agreement"
          },
          {
            "@language": "en",
            "@value": "MoU"
          },
          {
            "@language": "en",
            "@value": "access rights"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.agree.comp.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-61:

Test 61: Check contributor.role for data owner
----------------------------------------------

:Test ID: T-DCSC-061
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-061
:Implements: :ref:`Metric 54: Data Ownership Role Declared <own.co.2>`

Description
^^^^^^^^^^^

Checks that the `contributor.role` field is not blank and contains the value `owner`.

Input
^^^^^

`contributor.role` = owner in maDMP

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `contributor` entries in scope (at DMP level or dataset level, depending on your schema).
3. For each contributor, extract the `role` field value.
4. Check whether any `role` value is equal to `owner` or an equivalent ownership term as defined by your project's controlled vocabulary.
5. For any contributor with `role` = `owner`, verify that the associated identifying fields (e.g., `name`, `contributor_id`) are present and non-empty.
6. Return **pass** if at least one contributor has a non-blank `role` of `owner` with identifying information present; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-061",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check contributor.role for data owner"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that the contributor.role field is not blank and contains the value owner."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "data ownership"
          },
          {
            "@language": "en",
            "@value": "contributor role"
          },
          {
            "@language": "en",
            "@value": "data stewardship"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/own.co.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-62:

Test 62: Check contributor for author role when dataset type is software
------------------------------------------------------------------------

:Test ID: T-DCSC-062
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-062
:Implements: :ref:`Metric 55: Software Dataset Author Declared <soft.auth.co.3>`

Description
^^^^^^^^^^^

Checks if the dataset type is software, then verifies that at least one contributor is present as author.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and identify those where `type` is set to software or an equivalent value.
3. If no dataset is typed as software, return **pass** (metric is not applicable).
4. For each software dataset, locate associated `contributor` entries (at dataset level or DMP level, depending on your schema).
5. Check whether at least one contributor has a `role` value indicating authorship (e.g., `author`, `creator`, or equivalent term defined by your project's controlled vocabulary).
6. Return **pass** if at least one software dataset has a contributor with an authorship role; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-062",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check contributor for author role when dataset type is software"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the dataset type is software, then verifies that at least one contributor is present as author."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "software authorship"
          },
          {
            "@language": "en",
            "@value": "contributor role"
          },
          {
            "@language": "en",
            "@value": "software dataset"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/soft.auth.co.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-63:

Test 63: Check ethical_issues_exist for valid value
---------------------------------------------------

:Test ID: T-DCSC-063
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-063
:Implements: :ref:`Metric 56: Ethical Issues Status Declared <ethics.co.1>`

Description
^^^^^^^^^^^

Checks the `ethical_issues_exist` field for a valid value (`yes`, `no`, `unknown`).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate the `ethical_issues_exist` field at the DMP level.
3. Check whether the field is present and non-empty.
4. Verify that the value is one of the accepted controlled values: `yes`, `no`, or `unknown`.
5. Return **pass** if `ethical_issues_exist` is present and contains a valid value; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-063",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check ethical_issues_exist for valid value"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks the ethical_issues_exist field for a valid value (yes, no, unknown)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "ethical issues"
          },
          {
            "@language": "en",
            "@value": "ethics declaration"
          },
          {
            "@language": "en",
            "@value": "research ethics"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/ethics.co.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-64:

Test 64: Check ethical_issues_description is present when ethical_issues_exist is no
------------------------------------------------------------------------------------

:Test ID: T-DCSC-064
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-064
:Implements: :ref:`Metric 58: Justification for Absence of Ethical Issues <ethics.co.3>`

Description
^^^^^^^^^^^

Checks if a justification is provided when `ethical_issues_exist` = `no`, by verifying the presence of `ethical_issues_description`.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate the `ethical_issues_exist` field at the DMP level.
3. If `ethical_issues_exist` is not set to `no`, return **pass** (metric is not applicable).
4. If `ethical_issues_exist` is set to `no`, check whether the `ethical_issues_description` field is present and non-empty.
5. Return **pass** if `ethical_issues_description` is present and non-empty; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-064",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check ethical_issues_description is present when ethical_issues_exist is no"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if a justification is provided when ethical_issues_exist = no, by verifying the presence of ethical_issues_description."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "ethical issues"
          },
          {
            "@language": "en",
            "@value": "ethics justification"
          },
          {
            "@language": "en",
            "@value": "ethics description"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/ethics.co.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-65:

Test 65: Check data_access for open status
------------------------------------------

:Test ID: T-DCSC-065
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-065
:Implements: :ref:`Metric 59: Data Access Status Open for the Dataset <data.shar.op.1>`

Description
^^^^^^^^^^^

Checks that `data_access` is set to `open` (accepted values: `open`, `shared`, `closed`).

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries in scope.
3. For each dataset, check whether a `data_access` field is present.
4. Verify that the `data_access` value is set to `open`.
5. Return **pass** if at least one dataset has `data_access` set to `open`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-065",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check data_access for open status"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that data_access is set to open (accepted values: open, shared, closed)."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "open access"
          },
          {
            "@language": "en",
            "@value": "data access status"
          },
          {
            "@language": "en",
            "@value": "openness"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.shar.op.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-66:

Test 66: Check distribution is present for dataset
--------------------------------------------------

:Test ID: T-DCSC-066
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-066
:Implements: :ref:`Metric 60: Data License is Present <data.shar.co.1>`

Description
^^^^^^^^^^^

Checks that a `distribution` entry is present for the dataset.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries in scope.
3. For each dataset, check whether a `distribution` array or object is present and non-empty.
4. Return **pass** if at least one dataset contains a non-empty `distribution` entry; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-066",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check distribution is present for dataset"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that a distribution entry is present for the dataset."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "data licence"
          },
          {
            "@language": "en",
            "@value": "distribution"
          },
          {
            "@language": "en",
            "@value": "license reference"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.shar.co.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-67:

Test 67: Check license_ref is present within distribution
---------------------------------------------------------

:Test ID: T-DCSC-067
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-067
:Implements: :ref:`Metric 60: Data License is Present <data.shar.co.1>`

Description
^^^^^^^^^^^

Checks that a `license_ref` is present within the distribution entry.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `license_ref` field is present and non-empty.
4. Return **pass** if at least one distribution contains a non-empty `license_ref`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-067",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check license_ref is present within distribution"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that a license_ref is present within the distribution entry."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "data licence"
          },
          {
            "@language": "en",
            "@value": "distribution"
          },
          {
            "@language": "en",
            "@value": "license reference"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.shar.co.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-68:

Test 68: Check rights for data restrictions reference
-----------------------------------------------------

:Test ID: T-DCSC-068
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-068
:Implements: :ref:`Metric 61: Data Restrictions Reference <data.shar.co.2>`

Description
^^^^^^^^^^^

Checks if any data restrictions are referenced via the `rights` field in the maDMP.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `rights` field is present and non-empty.
4. Return **pass** if at least one distribution contains a non-empty `rights` value referencing data restrictions or access rights; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-068",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check rights for data restrictions reference"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if any data restrictions are referenced via the rights field in the maDMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "data restrictions"
          },
          {
            "@language": "en",
            "@value": "access rights"
          },
          {
            "@language": "en",
            "@value": "distribution"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.shar.co.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-69:

Test 69: Check distribution license_ref for Horizon Europe CC-BY compliance
---------------------------------------------------------------------------

:Test ID: T-DCSC-069
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-069
:Implements: :ref:`Metric 62: Dataset License Complies with Funder Requirements <data.shar.comp.1>`

Description
^^^^^^^^^^^

Checks if the maDMP `dataset.distribution.license_ref` matches Horizon Europe RDM requirements, i.e. CC-BY.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `license_ref` field is present and non-empty.
4. Verify that the `license_ref` value corresponds to a CC-BY licence URI or identifier (e.g., https://creativecommons.org/licenses/by/4.0/, or an equivalent CC-BY variant) as required by Horizon Europe RDM guidelines.
5. Return **pass** if at least one distribution contains a `license_ref` matching a CC-BY licence; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-069",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check distribution license_ref for Horizon Europe CC-BY compliance"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the maDMP dataset.distribution.license_ref matches Horizon Europe RDM requirements, i.e. CC-BY."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "funder licence"
          },
          {
            "@language": "en",
            "@value": "Horizon Europe"
          },
          {
            "@language": "en",
            "@value": "CC-BY"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.shar.comp.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-70:

Test 70: Check data_access matches destination host access policy
-----------------------------------------------------------------

:Test ID: T-DCSC-070
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-070
:Implements: :ref:`Metric 63: Repository Access Rights Consistency Aligned <data.shar.feas.1>`

Description
^^^^^^^^^^^

Checks if the dataset `data_access` value matches the access rights supported by the destination host in the maDMP.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and extract the `data_access` value for each.
3. For each dataset, locate the associated `distribution` objects and their `host` entries.
4. Extract any access-related fields from the `host` entry (e.g., `url`, `pid_system`, or access policy metadata) that indicate the access conditions supported by the destination repository.
5. Compare the dataset-level `data_access` value against the access policy of the destination host, checking for consistency (e.g., a dataset declared as `open` should be hosted at a repository that supports open access).
6. Return **pass** if at least one dataset has a `data_access` value that is consistent with its destination host access policy; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-070",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check data_access matches destination host access policy"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the dataset data_access value matches the access rights supported by the destination host in the maDMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "access rights"
          },
          {
            "@language": "en",
            "@value": "repository consistency"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.shar.feas.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-71:

Test 71: Check distribution license_ref matches destination host licence policy
-------------------------------------------------------------------------------

:Test ID: T-DCSC-071
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-071
:Implements: :ref:`Metric 64: Repository Data License Aligned with the DMP <data.shar.feas.2>`

Description
^^^^^^^^^^^

Checks if the data licence matches the destination by verifying `distribution.license.license_ref` against the destination host's licence policy in the maDMP.

Input
^^^^^

`distribution.license.license_ref` in maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, extract the `license_ref` value from the `license` object.
4. Identify the destination host for the same distribution and extract any licence-related metadata from the `host` entry (e.g., supported licence types, host URL, or policy references).
5. Compare the `license_ref` value against the licence policy of the destination host, checking for consistency.
6. Return **pass** if at least one distribution has a `license_ref` that is consistent with its destination host licence policy; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-071",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check distribution license_ref matches destination host licence policy"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the data licence matches the destination by verifying distribution.license.license_ref against the destination host licence policy in the maDMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "data licence"
          },
          {
            "@language": "en",
            "@value": "repository alignment"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.shar.feas.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-72:

Test 72: Check distribution license.start_date matches destination embargo policy
---------------------------------------------------------------------------------

:Test ID: T-DCSC-072
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-072
:Implements: :ref:`Metric 65: Embargo Implementation Alignment <data.shar.feas.3>`

Description
^^^^^^^^^^^

Checks if the embargo date matches the destination by verifying `distribution.license.start_date` against the destination host's embargo policy in the maDMP.

Input
^^^^^

`distribution.license.start_date` in maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, extract the `start_date` value from the `license` object.
4. Identify the destination host for the same distribution and extract any embargo-related metadata from the `host` entry (e.g., supported embargo periods, availability windows, or policy references).
5. Compare the `start_date` value against the embargo policy of the destination host, checking that the declared embargo period is supported by the repository.
6. Return **pass** if at least one distribution has a `license.start_date` that is consistent with its destination host embargo policy; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-072",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check distribution license.start_date matches destination embargo policy"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the embargo date matches the destination by verifying distribution.license.start_date against the destination host embargo policy in the maDMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "embargo"
          },
          {
            "@language": "en",
            "@value": "availability date"
          },
          {
            "@language": "en",
            "@value": "repository alignment"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.shar.feas.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-73:

Test 73: Check rights matches destination host restriction policy
-----------------------------------------------------------------

:Test ID: T-DCSC-073
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-073
:Implements: :ref:`Metric 66: Repository Data Restrictions <data.shar.feas.4>`

Description
^^^^^^^^^^^

Checks if the data restrictions match the destination by verifying the `rights` field against the destination host's restriction policy in the maDMP.

Input
^^^^^

`rights` in maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, extract the `rights` field value.
4. Identify the destination host for the same distribution and extract any restriction-related metadata from the `host` entry (e.g., supported access conditions, restriction policies, or host URL for policy lookup).
5. Compare the `rights` value against the restriction policy of the destination host, checking that the declared restrictions are consistent with what the repository supports.
6. Return **pass** if at least one distribution has a `rights` value that is consistent with its destination host restriction policy; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-073",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check rights matches destination host restriction policy"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the data restrictions match the destination by verifying the rights field against the destination host restriction policy in the maDMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "data restrictions"
          },
          {
            "@language": "en",
            "@value": "access rights"
          },
          {
            "@language": "en",
            "@value": "repository alignment"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.shar.feas.4"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-74:

Test 74: Check repository host for absence of embargo date
----------------------------------------------------------

:Test ID: T-DCSC-074
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-074
:Implements: :ref:`Metric 67: Embargo Declared in the DMP or Repository <data.shar.comp.2>`

Description
^^^^^^^^^^^

Checks that no embargo date field exists in the destination repository host entry, in compliance with Horizon Europe embargo policy.

Input
^^^^^

Repository host entry in maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, locate the `host` entry.
4. Check whether any embargo date field is present within the `host` entry.
5. Return **pass** if no embargo date field is found in any destination host entry; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-074",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check repository host for absence of embargo date"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that no embargo date field exists in the destination repository host entry, in compliance with Horizon Europe embargo policy."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "embargo"
          },
          {
            "@language": "en",
            "@value": "Horizon Europe"
          },
          {
            "@language": "en",
            "@value": "licence compliance"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.shar.comp.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-75:

Test 75: Check distribution.license.start_date for absence in maDMP
-------------------------------------------------------------------

:Test ID: T-DCSC-075
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-075
:Implements: :ref:`Metric 67: Embargo Declared in the DMP or Repository <data.shar.comp.2>`

Description
^^^^^^^^^^^

Checks that `distribution.license.start_date` is not set in the maDMP, in compliance with Horizon Europe embargo policy.

Input
^^^^^

`distribution.license.start_date` in maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `license` object is present containing a `start_date` field.
4. Return **pass** if no `distribution.license.start_date` field is present or set across all distributions; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-075",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check distribution.license.start_date for absence in maDMP"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that distribution.license.start_date is not set in the maDMP, in compliance with Horizon Europe embargo policy."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "embargo"
          },
          {
            "@language": "en",
            "@value": "Horizon Europe"
          },
          {
            "@language": "en",
            "@value": "licence compliance"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.shar.comp.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-76:

Test 76: Check host.title and host.url against thematic repository registries
-----------------------------------------------------------------------------

:Test ID: T-DCSC-076
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-076
:Implements: :ref:`Metric 68: Thematic Data Repositories Referenced <repo.co.3>`

Description
^^^^^^^^^^^

Checks if the repository `host.title` or `host.url` matches a thematic repository in the OpenAIRE Graph repositories API or another SKG API repository registry.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, extract the `host.title` and `host.url` values.
4. Query the OpenAIRE Graph repositories API (or an equivalent SKG API repository registry) using `host.title` or `host.url` as search parameters.
5. Check whether the returned results indicate that the referenced repository is classified as a thematic repository within the registry.
6. Return **pass** if at least one distribution's `host.title` or `host.url` matches a thematic repository entry in the registry; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-076",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check host.title and host.url against thematic repository registries"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the repository host.title or host.url matches a thematic repository in the OpenAIRE Graph repositories API or another SKG API repository registry."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "thematic repository"
          },
          {
            "@language": "en",
            "@value": "OpenAIRE"
          },
          {
            "@language": "en",
            "@value": "repository registry"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/repo.co.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-77:

Test 77: Check host against OpenAIRE and FAIRsharing FAIR benchmarks
--------------------------------------------------------------------

:Test ID: T-DCSC-077
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-077
:Implements: :ref:`Metric 69: Repository Conforms with FAIR Data Principles <repo.comp.2>`

Description
^^^^^^^^^^^

Checks if the repository declared in `host` is aligned with FAIR data principles by cross-referencing against benchmarks in OpenAIRE and FAIRsharing.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, extract the `host.title` and `host.url` values.
4. Query the OpenAIRE repository API using `host.title` or `host.url` to check whether the repository is listed and carries a FAIR-related assessment or endorsement.
5. Query the FAIRsharing registry using `host.title` or `host.url` to check whether the repository is listed and associated with FAIR data principles compliance.
6. Return **pass** if at least one distribution's host is found in either OpenAIRE or FAIRsharing with a FAIR benchmark or endorsement; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-077",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check host against OpenAIRE and FAIRsharing FAIR benchmarks"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the repository declared in host is aligned with FAIR data principles by cross-referencing against benchmarks in OpenAIRE and FAIRsharing."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "FAIR data principles"
          },
          {
            "@language": "en",
            "@value": "FAIRsharing"
          },
          {
            "@language": "en",
            "@value": "OpenAIRE"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/repo.comp.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-78:

Test 78: Check host against trusted repository registry benchmark
-----------------------------------------------------------------

:Test ID: T-DCSC-078
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-078
:Implements: :ref:`Metric 70: Trusted Repository is Used <repo.comp.3>`

Description
^^^^^^^^^^^

Checks if the repository declared in `host` is included in a trusted repository registry benchmark.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, extract the `host.title` and `host.url` values.
4. Query a recognised trusted repository registry (e.g., CoreTrustSeal certified repositories list, CLARIN centres, DINI certified repositories, or an equivalent benchmark) using `host.title` or `host.url` as search parameters.
5. Check whether the repository is listed and holds a valid trusted repository certification or endorsement.
6. Return **pass** if at least one distribution's host is found in a recognised trusted repository registry; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-078",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check host against trusted repository registry benchmark"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the repository declared in host is included in a trusted repository registry benchmark."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "trusted repository"
          },
          {
            "@language": "en",
            "@value": "CoreTrustSeal"
          },
          {
            "@language": "en",
            "@value": "repository certification"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/repo.comp.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-79:

Test 79: Check host.backup_frequency and host.backup_type for back-up strategy
------------------------------------------------------------------------------

:Test ID: T-DCSC-079
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-079
:Implements: :ref:`Metric 71: Verification of Back-up Strategy <repo.co.4>`

Description
^^^^^^^^^^^

Checks that a back-up strategy exists by verifying that `host.backup_frequency` and `host.backup_type` are present and non-empty in the maDMP.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, locate the `host` entry.
4. Check whether the `backup_frequency` field is present and non-empty within the `host` entry.
5. Check whether the `backup_type` field is present and non-empty within the same `host` entry.
6. Return **pass** if at least one host entry contains both a non-empty `backup_frequency` and a non-empty `backup_type`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-079",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check host.backup_frequency and host.backup_type for back-up strategy"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that a back-up strategy exists by verifying that host.backup_frequency and host.backup_type are present and non-empty in the maDMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "back-up strategy"
          },
          {
            "@language": "en",
            "@value": "backup frequency"
          },
          {
            "@language": "en",
            "@value": "repository"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/repo.co.4"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-80:

Test 80: Check certified_with exists in host
--------------------------------------------

:Test ID: T-DCSC-080
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-080
:Implements: :ref:`Metric 72: Certification of Repository <repo.co.5>`

Description
^^^^^^^^^^^

Checks that a `certified_with` field exists and is non-empty within the `host` entry of the maDMP.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, locate the `host` entry.
4. Check whether a `certified_with` field is present and non-empty within the `host` entry.
5. Return **pass** if at least one host entry contains a non-empty `certified_with` value; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-080",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check certified_with exists in host"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that a certified_with field exists and is non-empty within the host entry of the maDMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "repository certification"
          },
          {
            "@language": "en",
            "@value": "certified_with"
          },
          {
            "@language": "en",
            "@value": "repository"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/repo.co.5"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-81:

Test 81: Check cost title or description for preservation reference
-------------------------------------------------------------------

:Test ID: T-DCSC-081
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-081
:Implements: :ref:`Metric 73: Used Resources for Preservation <repo.co.7>`

Description
^^^^^^^^^^^

Checks if a `cost` entry with `currency_code`, `description`, `title`, and `value` includes a reference to preservation in its `title` or `description`.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `cost` entries at DMP level.
3. For each cost entry, check whether `currency_code` and `value` are present and non-empty.
4. Check whether the `title` or `description` field of the cost entry contains a term related to preservation (e.g., "preservation", "archiving", "long-term storage", or equivalent).
5. Return **pass** if at least one cost entry has non-empty `currency_code` and `value`, and a `title` or `description` referencing preservation; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-081",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check cost title or description for preservation reference"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if a cost entry with currency_code, description, title, and value includes a reference to preservation in its title or description."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "long-term preservation"
          },
          {
            "@language": "en",
            "@value": "cost"
          },
          {
            "@language": "en",
            "@value": "resources"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/repo.co.7"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-82:

Test 82: Check host_id against FAIRsharing for repository policy
----------------------------------------------------------------

:Test ID: T-DCSC-082
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-082
:Implements: :ref:`Metric 74: Repository Policy is Present <repo.co.6>`

Description
^^^^^^^^^^^

Checks if the repository identified by `host_id.identifier` and `host_id.type` in the maDMP has associated policies in FAIRsharing.

Input
^^^^^

maDMP JSON; FAIRsharing registry

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, extract the `host_id.identifier` and `host_id.type` values from the `host` entry.
4. Query the FAIRsharing registry using the extracted `host_id.identifier` and `host_id.type` to locate the corresponding repository record.
5. Check whether the FAIRsharing record for the repository contains one or more associated policy entries (e.g., via the `id_policy` field or equivalent policy linkage in the FAIRsharing API response).
6. Return **pass** if at least one distribution's host resolves to a FAIRsharing repository record with at least one associated policy; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-082",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check host_id against FAIRsharing for repository policy"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the repository identified by host_id.identifier and host_id.type in the maDMP has associated policies in FAIRsharing."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "repository policy"
          },
          {
            "@language": "en",
            "@value": "FAIRsharing"
          },
          {
            "@language": "en",
            "@value": "host identifier"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/repo.co.6"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-83:

Test 83: Check dataset_id resolves to declared destination via DOI URL
----------------------------------------------------------------------

:Test ID: T-DCSC-083
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-083
:Implements: :ref:`Metric 75: Repository Identifier Accuracy <repo.feas.1>`

Description
^^^^^^^^^^^

Checks if the reused dataset identifier in the maDMP matches the destination by resolving `dataset_id` against its DOI URL.

Input
^^^^^

`dataset_id` in maDMP JSON; DOI URL resolution

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and extract the `dataset_id` field (identifier and type) for each.
3. For each dataset, check whether the `dataset_id` value is present, non-empty, and of type DOI or resolvable identifier.
4. Resolve the `dataset_id` via its DOI URL (e.g., via https://doi.org/) and retrieve the landing page or metadata record.
5. Compare the resolved repository or hosting institution against the destination declared in the associated `distribution.host` entry.
6. Return **pass** if at least one dataset's `dataset_id` resolves to the declared destination repository; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-083",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check dataset_id resolves to declared destination via DOI URL"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the reused dataset identifier in the maDMP matches the destination by resolving dataset_id against its DOI URL."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "dataset identifier"
          },
          {
            "@language": "en",
            "@value": "DOI"
          },
          {
            "@language": "en",
            "@value": "repository destination"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/repo.feas.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-84:

Test 84: Check preservation_statement and host for long-term storage intention
------------------------------------------------------------------------------

:Test ID: T-DCSC-084
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-084
:Implements: :ref:`Metric 76: Long-Term Preservation Dataset <repo.feas.2>`

Description
^^^^^^^^^^^

Checks the dataset `preservation_statement` and `host` fields to verify that the dataset is intended to be archived in a long-term storage repository.

Input
^^^^^

`preservation_statement` in maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, check whether a `preservation_statement` field is present and non-empty within the `host` entry.
4. Check whether the same distribution contains a `host` entry with at least a `title` or `url` identifying a destination repository.
5. Return **pass** if at least one distribution contains both a non-empty `preservation_statement` and a declared destination `host`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-084",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check preservation_statement and host for long-term storage intention"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks the dataset preservation_statement and host fields to verify that the dataset is intended to be archived in a long-term storage repository."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "long-term preservation"
          },
          {
            "@language": "en",
            "@value": "preservation statement"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/repo.feas.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-85:

Test 85: Check dataset.keyword against Zenodo keywords
------------------------------------------------------

:Test ID: T-DCSC-085
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-085
:Implements: :ref:`Metric 77: Dataset Characteristics Are Compatible with the Repository <repo.feas.4>`

Description
^^^^^^^^^^^

Checks if the repository has the appropriate characteristics by verifying that `dataset.keyword` values in the maDMP match keywords supported or indexed in Zenodo.

Input
^^^^^

`dataset.keyword` in maDMP JSON; Zenodo keyword index

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and extract the `keyword` field values for each.
3. If no `keyword` values are present, return **fail**.
4. Query the Zenodo API using the extracted keyword values to check whether they are recognised or indexed within Zenodo's subject or keyword metadata.
5. Return **pass** if at least one dataset's `keyword` values match keywords supported or indexed in Zenodo; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-085",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check dataset.keyword against Zenodo keywords"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the repository has the appropriate characteristics by verifying that dataset.keyword values in the maDMP match keywords supported or indexed in Zenodo."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "repository appropriateness"
          },
          {
            "@language": "en",
            "@value": "Zenodo"
          },
          {
            "@language": "en",
            "@value": "dataset keyword"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/repo.feas.4"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-86:

Test 86: Check dataset.language against Zenodo language support
---------------------------------------------------------------

:Test ID: T-DCSC-086
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-086
:Implements: :ref:`Metric 77: Dataset Characteristics Are Compatible with the Repository <repo.feas.4>`

Description
^^^^^^^^^^^

Checks if the repository has the appropriate characteristics by verifying that `dataset.language` in the maDMP matches a language supported by Zenodo.

Input
^^^^^

`dataset.language` in maDMP JSON; Zenodo language support

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and extract the `language` field value for each.
3. If no `language` value is present, return **fail**.
4. Query the Zenodo API or consult Zenodo's supported language list to check whether the declared `language` value is recognised and supported by Zenodo.
5. Return **pass** if at least one dataset's `language` value matches a language supported by Zenodo; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-086",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check dataset.language against Zenodo language support"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the repository has the appropriate characteristics by verifying that dataset.language in the maDMP matches a language supported by Zenodo."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "repository appropriateness"
          },
          {
            "@language": "en",
            "@value": "Zenodo"
          },
          {
            "@language": "en",
            "@value": "dataset language"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/repo.feas.4"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-87:

Test 87: Check host_id against Zenodo and FAIRsharing for policy compliance
---------------------------------------------------------------------------

:Test ID: T-DCSC-087
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-087
:Implements: :ref:`Metric 70: Trusted Repository is Used <repo.comp.3>`

Description
^^^^^^^^^^^

Checks if the repository is aligned with policies and registry entries by cross-referencing `host_id.identifier` and `host_id.type` against repository records in Zenodo and FAIRsharing.

Input
^^^^^

`host_id.identifier` and `host_id.type` in maDMP JSON; Zenodo repository records; FAIRsharing registry

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, extract the `host_id.identifier` and `host_id.type` values from the `host` entry.
4. Query the Zenodo API using the extracted identifier to check whether the repository is listed and has associated policy or compliance metadata.
5. Query the FAIRsharing registry using the extracted identifier to check whether the repository record contains associated policy entries or compliance information.
6. Return **pass** if at least one distribution's host resolves to a matching record in either Zenodo or FAIRsharing with associated policy compliance information; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-087",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check host_id against Zenodo and FAIRsharing for policy compliance"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the repository is aligned with policies and registry entries by cross-referencing host_id.identifier and host_id.type against repository records in Zenodo and FAIRsharing."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "repository policy compliance"
          },
          {
            "@language": "en",
            "@value": "FAIRsharing"
          },
          {
            "@language": "en",
            "@value": "Zenodo"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/repo.comp.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-88:

Test 88: Check related_identifier.identifier for external resources
-------------------------------------------------------------------

:Test ID: T-DCSC-088
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-088
:Implements: :ref:`Metric 78: Data External Resources Included in the DMP <data.exteresource.co.1>`

Description
^^^^^^^^^^^

Checks if there are external resources declared in the DMP by verifying the presence of `related_identifier.identifier` entries.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and check for the presence of a `related_identifier` array or object.
3. For each `related_identifier` entry, check whether the `identifier` field is present and non-empty.
4. Return **pass** if at least one dataset contains a `related_identifier` entry with a non-empty `identifier` field; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-088",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check related_identifier.identifier for external resources"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if there are external resources declared in the DMP by verifying the presence of related_identifier.identifier entries."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "external resources"
          },
          {
            "@language": "en",
            "@value": "related identifier"
          },
          {
            "@language": "en",
            "@value": "completeness"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.exteresource.co.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-89:

Test 89: Check related_identifier for metadata standard fields
--------------------------------------------------------------

:Test ID: T-DCSC-089
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-089
:Implements: :ref:`Metric 79: Metadata Standard Specified in the DMP <data.exteresource.co.2>`

Description
^^^^^^^^^^^

Checks if a metadata format or standard is listed in the DMP by verifying that `related_identifier.metadata_scheme`, `related_identifier.scheme_type`, and `related_identifier.scheme_uri` are present and non-empty.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and check for the presence of a `related_identifier` array or object.
3. For each `related_identifier` entry, check whether `metadata_scheme`, `scheme_type`, and `scheme_uri` fields are all present and non-empty.
4. Return **pass** if at least one dataset contains a `related_identifier` entry with non-empty values for all three fields; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-089",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check related_identifier for metadata standard fields"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if a metadata format or standard is listed in the DMP by verifying that related_identifier.metadata_scheme, related_identifier.scheme_type, and related_identifier.scheme_uri are present and non-empty."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "metadata standard"
          },
          {
            "@language": "en",
            "@value": "metadata scheme"
          },
          {
            "@language": "en",
            "@value": "completeness"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.exteresource.co.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-90:

Test 90: Check URLs in maDMP are valid and resolvable
-----------------------------------------------------

:Test ID: T-DCSC-090
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-090
:Implements: :ref:`Metric 80: Resolvable External Resources <data.exteresource.feas.1>`

Description
^^^^^^^^^^^

Checks if all included URLs in the maDMP are syntactically valid and resolve to accessible resources.

Input
^^^^^

URLs in maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Extract all URL values present across the document (e.g., from `related_identifier.identifier`, `host.url`, `distribution.access_url`, and any other URL-bearing fields).
3. For each extracted URL, validate its syntax against standard URL format rules.
4. Attempt to resolve each syntactically valid URL via an HTTP request and check whether it returns a successful response (e.g., HTTP 200 or 3xx redirect to a valid resource).
5. Return **pass** if at least one URL is both syntactically valid and successfully resolvable; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-090",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check URLs in maDMP are valid and resolvable"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if all included URLs in the maDMP are syntactically valid and resolve to accessible resources."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "resolvable URLs"
          },
          {
            "@language": "en",
            "@value": "external resources"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.exteresource.feas.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-91:

Test 91: Check dataset fields against OpenAIRE SKG-IF API
---------------------------------------------------------

:Test ID: T-DCSC-091
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-091
:Implements: :ref:`Metric 81: OpenAIRE Mentioned Dataset Validation <data.exteresource.feas.2>`

Description
^^^^^^^^^^^

Checks if datasets declared in the maDMP are found in the OpenAIRE SKG-IF API by querying with `dataset_id.identifier`, `dataset_id.type`, `dataset.title`, and `dataset.type`.

Input
^^^^^

`dataset_id.identifier`, `dataset_id.type`, `dataset.title`, `dataset.type` in maDMP JSON; OpenAIRE SKG-IF API

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and extract `dataset_id.identifier`, `dataset_id.type`, `dataset.title`, and `dataset.type` for each.
3. For each dataset, query the OpenAIRE SKG-IF API using the extracted identifier (preferring `dataset_id.identifier` and `dataset_id.type`) to search for a matching record.
4. If no match is found by identifier, retry the query using `dataset.title` and `dataset.type` as search parameters.
5. Check whether the API response contains a record that corresponds to the declared dataset.
6. Return **pass** if at least one dataset produces a matching record in the OpenAIRE SKG-IF API; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-091",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check dataset fields against OpenAIRE SKG-IF API"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if datasets declared in the maDMP are found in the OpenAIRE SKG-IF API by querying with dataset_id.identifier, dataset_id.type, dataset.title, and dataset.type."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "OpenAIRE"
          },
          {
            "@language": "en",
            "@value": "SKG-IF"
          },
          {
            "@language": "en",
            "@value": "dataset validation"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.exteresource.feas.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-92:

Test 92: Check contributor roles against CRediT taxonomy
--------------------------------------------------------

:Test ID: T-DCSC-092
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-092
:Implements: :ref:`Metric 82: Contributor Roles Follow CRediT Taxonomy <data.exteresource.feas.3>`

Description
^^^^^^^^^^^

Checks if the dataset uses the CRediT taxonomy by verifying that `contributor` role values in the maDMP match recognised CRediT taxonomy terms.

Input
^^^^^

`contributor` in maDMP JSON; CRediT taxonomy

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `contributor` entries at DMP or dataset level and extract the `role` value for each.
3. If no `contributor` entries or `role` values are present, return **fail**.
4. Compare each extracted `role` value against the list of recognised CRediT taxonomy role terms (e.g., Conceptualization, Data Curation, Formal Analysis, Funding Acquisition, Investigation, Methodology, Project Administration, Resources, Software, Supervision, Validation, Visualization, Writing – Original Draft, Writing – Review & Editing).
5. Return **pass** if at least one contributor's `role` value matches a recognised CRediT taxonomy term; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-092",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check contributor roles against CRediT taxonomy"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the dataset uses the CRediT taxonomy by verifying that contributor role values in the maDMP match recognised CRediT taxonomy terms."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "CRediT taxonomy"
          },
          {
            "@language": "en",
            "@value": "contributor roles"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.exteresource.feas.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-93:

Test 93: Check host.pid_system for PID declaration
--------------------------------------------------

:Test ID: T-DCSC-093
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-093
:Implements: :ref:`Metric 83: Repository Supports Persistent Identifiers for Datasets <data.pid.cov.1>`

Description
^^^^^^^^^^^

Checks if the dataset has a PID by verifying that `host.pid_system` is present and non-empty in the maDMP.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, locate the `host` entry.
4. Check whether a `pid_system` field is present and non-empty within the `host` entry.
5. Return **pass** if at least one host entry contains a non-empty `pid_system` value; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-093",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check host.pid_system for PID declaration"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the dataset has a PID by verifying that host.pid_system is present and non-empty in the maDMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "persistent identifier"
          },
          {
            "@language": "en",
            "@value": "PID"
          },
          {
            "@language": "en",
            "@value": "coverage"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.pid.cov.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-94:

Test 94: Check certified_with against trusted registry
------------------------------------------------------

:Test ID: T-DCSC-094
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-094
:Implements: :ref:`Metric 84: Trusted Repository Referenced <data.pid.cov.2>`

Description
^^^^^^^^^^^

Checks if the repository is listed in a trusted registry by verifying the `certified_with` field in the maDMP.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, locate the `host` entry and extract the `certified_with` field value.
4. Check whether the `certified_with` value is present, non-empty, and corresponds to a recognised trusted registry (e.g., CoreTrustSeal, CLARIN, DINI, or equivalent).
5. Return **pass** if at least one host entry contains a `certified_with` value matching a trusted registry; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-094",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check certified_with against trusted registry"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the repository is listed in a trusted registry by verifying the certified_with field in the maDMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "trusted repository"
          },
          {
            "@language": "en",
            "@value": "certification"
          },
          {
            "@language": "en",
            "@value": "coverage"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.pid.cov.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-95:

Test 95: Check host_id.identifier and host_id.type for valid repository link
----------------------------------------------------------------------------

:Test ID: T-DCSC-095
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-095
:Implements: :ref:`Metric 84: Trusted Repository Referenced <data.pid.cov.2>`

Description
^^^^^^^^^^^

Checks if a valid link to the repository is provided by verifying that `host_id.identifier` and `host_id.type` are present, non-empty, and resolvable in the maDMP.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, extract `host_id.identifier` and `host_id.type` from the `host` entry.
4. Check whether both `host_id.identifier` and `host_id.type` are present and non-empty.
5. Attempt to resolve the `host_id.identifier` value as a URL or persistent identifier to confirm it leads to a valid, accessible repository resource.
6. Return **pass** if at least one distribution's `host_id.identifier` and `host_id.type` are present and the identifier resolves successfully; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-095",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check host_id.identifier and host_id.type for valid repository link"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if a valid link to the repository is provided by verifying that host_id.identifier and host_id.type are present, non-empty, and resolvable in the maDMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "repository link"
          },
          {
            "@language": "en",
            "@value": "host identifier"
          },
          {
            "@language": "en",
            "@value": "coverage"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.pid.cov.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-96:

Test 96: Check host.pid_system matches destination PID system in Zenodo
-----------------------------------------------------------------------

:Test ID: T-DCSC-096
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-096
:Implements: :ref:`Metric 85: Dataset PID System in the DMP Matches the Repository <data.pid.feas.1>`

Description
^^^^^^^^^^^

Checks if the PID system declared in `host.pid_system` matches the PID system provided by the destination repository, cross-referenced against Zenodo DOI metadata.

Input
^^^^^

`host.pid_system` in maDMP JSON; Zenodo DOI metadata

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate dataset entries and their associated `distribution` objects or arrays.
3. For each distribution, extract the `host.pid_system` value and the destination repository identifier from the `host` entry.
4. Query the Zenodo API using the destination repository identifier to retrieve the repository's supported PID system (e.g., DOI assignment via Zenodo).
5. Compare the `host.pid_system` value against the PID system confirmed as supported by the destination repository in Zenodo.
6. Return **pass** if at least one distribution's `host.pid_system` matches the PID system provided by its declared destination in Zenodo; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-096",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check host.pid_system matches destination PID system in Zenodo"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if the PID system declared in host.pid_system matches the PID system provided by the destination repository, cross-referenced against Zenodo DOI metadata."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "persistent identifier"
          },
          {
            "@language": "en",
            "@value": "Zenodo"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/data.pid.feas.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-97:

Test 97: Check dmp.contributor name, role, and contact
------------------------------------------------------

:Test ID: T-DCSC-097
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-097
:Implements: :ref:`Metric 87: Research Data Management Roles Declared <role.co.1>`

Description
^^^^^^^^^^^

Checks that `dmp.contributor.name`, `dmp.contributor.role`, and `dmp.contributor.contact` are present and non-empty in the maDMP.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `contributor` entries at DMP level.
3. For each contributor entry, check whether `name`, `role`, and `contact` fields are all present and non-empty.
4. Return **pass** if at least one contributor entry contains non-empty values for all three of `name`, `role`, and `contact`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-097",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check dmp.contributor name, role, and contact"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that dmp.contributor.name, dmp.contributor.role, and dmp.contributor.contact are present and non-empty in the maDMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "contributor roles"
          },
          {
            "@language": "en",
            "@value": "RDM roles"
          },
          {
            "@language": "en",
            "@value": "completeness"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/role.co.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-98:

Test 98: Check dmp.contributor.role for Data Steward
----------------------------------------------------

:Test ID: T-DCSC-098
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-098
:Implements: :ref:`Metric 88: DMP Validation by Data Steward <dmp.valid.co.2>`

Description
^^^^^^^^^^^

Checks that at least one `dmp.contributor.role` value equals `Data Steward` in the maDMP.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `contributor` entries at DMP level.
3. For each contributor entry, extract the `role` field value.
4. Check whether any `role` value matches `Data Steward` (case-insensitive).
5. Return **pass** if at least one contributor entry has a `role` value of `Data Steward`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-098",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check dmp.contributor.role for Data Steward"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that at least one dmp.contributor.role value equals Data Steward in the maDMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "Data Steward"
          },
          {
            "@language": "en",
            "@value": "DMP validation"
          },
          {
            "@language": "en",
            "@value": "completeness"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/dmp.valid.co.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-99:

Test 99: Check contributor_id and affiliation.affiliation_id for PIDs
---------------------------------------------------------------------

:Test ID: T-DCSC-099
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-099
:Implements: :ref:`Metric 89: Contributors and Organisations PIDs <role.pid.co.1>`

Description
^^^^^^^^^^^

Checks that `contributor.contributor_id` and `contributor.affiliation.affiliation_id` are present and non-empty in the maDMP.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `contributor` entries at DMP level.
3. For each contributor entry, check whether `contributor_id` is present and non-empty.
4. For the same contributor entry, check whether `affiliation.affiliation_id` is present and non-empty within at least one affiliated organisation entry.
5. Return **pass** if at least one contributor entry contains both a non-empty `contributor_id` and a non-empty `affiliation.affiliation_id`; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-099",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check contributor_id and affiliation.affiliation_id for PIDs"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that contributor.contributor_id and contributor.affiliation.affiliation_id are present and non-empty in the maDMP."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "contributor PID"
          },
          {
            "@language": "en",
            "@value": "affiliation PID"
          },
          {
            "@language": "en",
            "@value": "completeness"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/role.pid.co.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-100:

Test 100: Check dmp.contributor fields against destination contributors
-----------------------------------------------------------------------

:Test ID: T-DCSC-100
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-100
:Implements: :ref:`Metric 90: Referenced RDM Roles <role.feas.1>`

Description
^^^^^^^^^^^

Checks that the roles of the contributors declared in the maDMP are mentioned in the destination by cross-referencing `dmp.contributor.name`, `dmp.contributor.role`, and `dmp.contributor.contact` against `contributors.name` and `contributors.type` in the destination.

Input
^^^^^

`dmp.contributor.name`, `dmp.contributor.role`, `dmp.contributor.contact` in maDMP JSON; `contributors.name`, `contributors.type` in destination metadata

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `contributor` entries at DMP level and extract `name`, `role`, and `contact` for each.
3. If no contributor entries or required fields are present, return **fail**.
4. Retrieve contributor metadata from the destination, extracting `contributors.name` and `contributors.type` entries.
5. For each contributor declared in the maDMP, attempt to match `dmp.contributor.name` against `contributors.name` and `dmp.contributor.role` against `contributors.type` in the destination.
6. Return **pass** if at least one maDMP contributor can be matched by name and role type in the destination contributor metadata; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-100",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check dmp.contributor fields against destination contributors"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that the roles of the contributors declared in the maDMP are mentioned in the destination by cross-referencing dmp.contributor.name, dmp.contributor.role, and dmp.contributor.contact against contributors.name and contributors.type in the destination."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "contributor roles"
          },
          {
            "@language": "en",
            "@value": "RDM roles"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/role.feas.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-101:

Test 101: Check Data Steward role in maDMP against contributors.type Other in destination
-----------------------------------------------------------------------------------------

:Test ID: T-DCSC-101
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-101
:Implements: :ref:`Metric 91: Data Steward Contribution Reflected in the Destination Repository <role.feas.2>`

Description
^^^^^^^^^^^

Checks that the contribution of a Data Steward is referenced in the destination by verifying that `dmp.contributor.role` equals `Data Steward` in the maDMP and a corresponding `contributors.type` of `Other` is present in the destination.

Input
^^^^^

`dmp.contributor.role` in maDMP JSON; `contributors.type` in destination metadata

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `contributor` entries at DMP level and extract the `role` field value for each.
3. Check whether at least one contributor entry has a `role` value of `Data Steward` (case-insensitive).
4. If no `Data Steward` role is found, return **fail**.
5. Retrieve contributor metadata from the destination and extract `contributors.type` values.
6. Check whether at least one `contributors.type` entry in the destination has a value of `Other`.
7. Return **pass** if both a `Data Steward` role is declared in the maDMP and a `contributors.type` of `Other` is present in the destination; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-101",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check Data Steward role in maDMP against contributors.type Other in destination"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that the contribution of a Data Steward is referenced in the destination by verifying that dmp.contributor.role equals Data Steward in the maDMP and a corresponding contributors.type of Other is present in the destination."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "Data Steward"
          },
          {
            "@language": "en",
            "@value": "DMP validation"
          },
          {
            "@language": "en",
            "@value": "feasibility"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/role.feas.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-102:

Test 102: Check contributor PIDs in maDMP against Zenodo contributors
---------------------------------------------------------------------

:Test ID: T-DCSC-102
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-102
:Implements: :ref:`Metric 92: Contributor and Organisation PIDs Match the Destination Repository <role.feas.3>`

Description
^^^^^^^^^^^

Checks if each contributor entry includes a valid PID in the destination by cross-referencing `contributor.affiliation.affiliation_id` and `contributor.contributor_id` in the maDMP against `contributors.affiliation` and `contributors.orcid` in Zenodo.

Input
^^^^^

`contributor.affiliation.affiliation_id` and `contributor.contributor_id` in maDMP JSON; `contributors.affiliation` and `contributors.orcid` in Zenodo

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `contributor` entries at DMP level and extract `contributor_id` and `affiliation.affiliation_id` for each.
3. If no contributor entries or required PID fields are present, return **fail**.
4. Query the Zenodo API for the relevant dataset record and retrieve `contributors.orcid` and `contributors.affiliation` values.
5. For each contributor declared in the maDMP, attempt to match `contributor.contributor_id` against `contributors.orcid` and `contributor.affiliation.affiliation_id` against `contributors.affiliation` in the Zenodo record.
6. Return **pass** if at least one contributor's PIDs are matched in the Zenodo destination record; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-102",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check contributor PIDs in maDMP against Zenodo contributors"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks if each contributor entry includes a valid PID in the destination by cross-referencing contributor.affiliation.affiliation_id and contributor.contributor_id in the maDMP against contributors.affiliation and contributors.orcid in Zenodo."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "contributor PID"
          },
          {
            "@language": "en",
            "@value": "affiliation PID"
          },
          {
            "@language": "en",
            "@value": "Zenodo"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/role.feas.3"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-103:

Test 103: Check cost in maDMP against repository cost
-----------------------------------------------------

:Test ID: T-DCSC-103
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-103
:Implements: :ref:`Metric 92: Contributor and Organisation PIDs Match the Destination Repository <role.feas.3>`

Description
^^^^^^^^^^^

Checks the cost of the repository by verifying that the `cost` declared in the maDMP is consistent with the actual cost of the destination repository.

Input
^^^^^

`cost` in maDMP JSON; repository cost information

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `cost` entries at DMP level and extract `currency_code`, `value`, `title`, and `description` for each.
3. If no `cost` entries are present, return **fail**.
4. Identify the destination repository from the associated `distribution.host` entries.
5. Retrieve the actual cost information for the destination repository from the repository's pricing documentation or API.
6. Compare the declared `cost.value` and `cost.currency_code` in the maDMP against the actual repository cost.
7. Return **pass** if at least one declared cost entry is consistent with the actual cost of the destination repository; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-103",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check cost in maDMP against repository cost"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks the cost of the repository by verifying that the cost declared in the maDMP is consistent with the actual cost of the destination repository."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "repository cost"
          },
          {
            "@language": "en",
            "@value": "cost"
          },
          {
            "@language": "en",
            "@value": "compliance"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/cost.comp.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-104:

Test 104: Check cost fields for budget specification
----------------------------------------------------

:Test ID: T-DCSC-104
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-104
:Implements: :ref:`Metric 93: DMP Includes a Budget for Personnel and Monetary Resources <cost.co.1>`

Description
^^^^^^^^^^^

Checks that the `cost` field in the maDMP is present and contains the required budget information for PMs and monetary resources.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `cost` entries at DMP level.
3. For each cost entry, check whether `currency_code`, `value`, `title`, and `description` are all present and non-empty.
4. Return **pass** if at least one `cost` entry contains non-empty values for all required fields; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-104",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check cost fields for budget specification"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks that the cost field in the maDMP is present and contains the required budget information for PMs and monetary resources."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "budget"
          },
          {
            "@language": "en",
            "@value": "cost"
          },
          {
            "@language": "en",
            "@value": "completeness"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/cost.co.1"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }


----

.. _dmp-test-105:

Test 105: Check cost in maDMP for no additional resources statement
-------------------------------------------------------------------

:Test ID: T-DCSC-105
:Persistent URI: https://w3id.org/dmp/evaluation/test/T-DCSC-105
:Implements: :ref:`Metric 94: DMP States No Additional RDM Resources Are Required <cost.co.2>`

Description
^^^^^^^^^^^

Checks the `cost` field in the maDMP to verify that it explicitly states that no additional resources are needed for data management activities.

Input
^^^^^

maDMP JSON

Output
^^^^^^

pass/fail

Procedure
^^^^^^^^^

1. Parse the maDMP JSON document.
2. Locate `cost` entries at DMP level.
3. If no `cost` entries are present, return **fail**.
4. For each cost entry, inspect the `title` and `description` fields for explicit statements indicating that no additional resources are required (e.g., phrases such as "no additional resources", "no extra costs", "within existing budget", or equivalent).
5. Return **pass** if at least one `cost` entry contains a `title` or `description` that explicitly states no additional resources are needed; otherwise return **fail**.

JSON-LD
^^^^^^^

.. toggle::

   .. code-block:: json

      {
        "@context": "https://w3id.org/ftr/context",
        "@id": "https://w3id.org/dmp/evaluation/test/T-DCSC-105",
        "@type": "ftr:Test",
        "dcterms:identifier": "T-DCSC",
        "dcterms:title": {
          "@language": "en",
          "@value": "Check cost in maDMP for no additional resources statement"
        },
        "dcterms:description": {
          "@language": "en",
          "@value": "Checks the cost field in the maDMP to verify that it explicitly states that no additional resources are needed for data management activities."
        },
        "dcat:keyword": [
          {
            "@language": "en",
            "@value": "no additional resources"
          },
          {
            "@language": "en",
            "@value": "RDM costs"
          },
          {
            "@language": "en",
            "@value": "completeness"
          },
          {
            "@language": "en",
            "@value": "maDMP"
          }
        ],
        "vivo:abbreviation": {
          "@value": "T-DCSC-T"
        },
        "dcterms:license": {
          "@id": "http://creativecommons.org/licenses/by/4.0/"
        },
        "dcat:version": {
          "@value": "0.0.1"
        },
        "adms:versionNotes": {
          "@language": "en",
          "@value": "Initial template version"
        },
        "ftr:status": {
          "@language": "en",
          "@value": "Draft"
        },
        "dcat:publisher": {
          "@id": "https://ostrails.eu"
        },
        "sio:SIO_000233": {
          "@id": "https://w3id.org/dmp/evaluation/metric/cost.co.2"
        },
        "dpv:isApplicableFor": {
          "@id": "https://schema.org/Dataset"
        }
      }

