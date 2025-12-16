Science Europe maDMP mapping
============================

We performed a mapping for each section using te Evaluation Rubric of the Science Europe template.

Section:  GENERAL INFORMATION
-----------------------------

.. list-table:: Subsection: Administrative information
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Provide information such as name of applicant, project number (if applicable), funding programme, version of DMP.
      - This section contains the minimal information required to identify the applicant and the references of the project.
      - dmp/contact/name,
        dmp/project/number,
        dmp/project/description,
        dmp/project/funding/funder_id,
        dmp/project/funding/grant_id
      -

Section:  1 DATA DESCRIPTION AND COLLECTION OR RE-USE OF EXISTING DATA
----------------------------------------------------------------------

.. list-table:: Subsection: 1a How will new data be collected or produced and/or how will existing data be re-used?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Explain which methodologies or software will be used if new data are collected or produced.
      - Gives clear details of where the existing data come from and how new data will be collected or produced. It clearly explains methods and software used.
      -
      - dataset/methodology
    * - State any constraints on re-use of existing data if there are any.
      - Explains, if existing data are re-used, how these data will be accessed and any constraints on their re-use.
      - ditribution/data_access,
        dmp/ethical_issues_exist,
        dataset/is_reused,
        dataset/security_and_privacy
      - dataset/is_reused,
        distribution/restriction_explanation
    * - Explain how data provenance will be documented.
      - Explains clearly, if applicable, why new data must be collected, rather than re-using existing data.
      - dataset/data_quality_assurance
      -
    * - Briefly state the reasons if the re-use of any existing data sources has been considered but discarded.
      - Explains clearly, if applicable, why new data must be collected, rather than re-using existing data.
      -
      - dataset/methodology

.. list-table:: Subsection: 1b What data (for example the kind, formats, and volumes), will be collected or produced?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Give details on the kind of data: for example, numeric (databases, spreadsheets), textual (documents), image, audio, video, and/or mixed media.
      - Clearly describes or lists what data types will be generated (for example numeric, textual, audio, or video) and their associated data formats, including, if needed, data conversion strategies.
      - dataset/type,
        dataset/description
      -
    * - Give details on the data format: the way in which the data is encoded for storage, often reflected by the filename extension (for example pdf, xls, doc, txt, or rdf).
      - Explains why certain formats have been chosen and indicates if they are in open and standard format. If a proprietary format is used, it explains why
      - dataset/format
        distribution/format
      -
    * - Justify the use of certain formats. For example, decisions may be based on staff expertise within the host organisation, a preference for open formats, standards accepted by data repositories, widespread usage within the research community, or on the software or equipment that will be used.
      - Explains why certain formats have been chosen and indicates if they are in open and standard format. If a proprietary format is used, it explains why
      - distribution/description
      - distribution/format_justification
    * - Give preference to open and standard formats as they facilitate sharing and long-term re-use of data (several repositories provide lists of such ‘preferred formats’).
      - Explains why certain formats have been chosen and indicates if they are in open and standard format. If a proprietary format is used, it explains why
      - distribution/format
      -
    * - Give details on the volumes (they can be expressed in storage space required (bytes), and/or in numbers of objects, files, rows, and columns).
      - Provides information about the estimated data volume.
      - distribution/byte_size
      -


Section:  2 DOCUMENTATION AND DATA QUALITY
------------------------------------------

.. list-table:: Subsection: 2a What metadata and documentation (for example the methodology of data collection and way of organising data) will accompany the data?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Indicate which metadata will be provided to help others identify and discover the data.
      - Clearly outlines the metadata that will accompany the data, with reference to good practice in the community (for example uses metadata standards where they exist).
      - dataset/metadata
      -
    * - Indicate which metadata standards (for example DDI, TEI, EML, MARC, CMDI) will be used.
      - Clearly outlines the documentation needed to enable data re-use, stating where the information will be recorded (for example a database with links to each item, a ‘readme’ text file, file headers, code books, or lab notebooks).
      - dataset/metadata
      -
    * - Use community metadata standards where these are in place.
      -
      - dataset/metadata
      -
    * - Indicate how the data will be organised during the project mentioning, for example, conventions, version control, and folder structures. Consistent, well-ordered research data will be easier to find, understand, and reuse.
      - Indicates how the data will be organised during the project (for example naming conventions, version control strategy and folder structures).
      - dataset/metadata,
        dataset/keyword,
        dataset/data_quality_assurance
      -
    * - Consider what other documentation is needed to enable re-use. This may include information on the methodology used to collect the data, analytical and procedural information, definitions of variables, units of measurement, and so on.
      -
      -
      - dataset/methodology
    * - Consider how this information will be captured and where it will be recorded (for example in a database with links to each item, a ’readme’ text file, file headers, code books, or lab notebooks).
      -
      -
      - dataset/metadata/description,
        distribution/host/*

.. list-table:: Subsection: 2b What data quality control measures will be used?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Explain how the consistency and quality of data collection will be controlled and documented. This may include processes such as calibration, repeated samples or measurements, standardised data capture, data entry validation, peer review of data, or representation with controlled vocabularies.
      - Clearly describes the approach taken to ensure and document quality control in the collection of data during the lifetime of the project.
      - dataset/data_quality_assurance
      -


Section:  3 STORAGE AND BACKUP DURING THE RESEARCH PROCESS
----------------------------------------------------------

.. list-table:: Subsection: 3a How will data and metadata be stored and backed up during the research?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Describe where the data will be stored and backed up during research activities and how often the backup will be performed. It is recommended to store data in least at two separate locations.
      - Clearly (even if briefly) describes:
        the location where the data and backups will be stored during the research activities.
        how often backups will be performed.
        the use of robust, managed storage with automatic backup (for example storage provided by the home institution).
      - host/backup_type
        host/backup_frequency
      -
    * - Give preference to the use of robust, managed storage with automatic backup, such as provided by IT support services of the home institution. Storing data on laptops, stand-alone hard drives, or external storage devices such as USB sticks is not recommended.
      - Explains why institutional storage will not be used (and for what part of the data) and describes the (additional) locations, storage media, and procedures that will be used for storing and backing up data during the project.
      - dataset/distribution/host/*
      -


.. list-table:: Subsection: 3b How will data security and protection of sensitive data be taken care of during the research?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Explain how the data will be recovered in the event of an incident.
      - Clearly explains
        how the data will be recovered in the event of an incident.
      -
      - host/description
        host/data_recovery_explanation
    * - Explain who will have access to the data during the research and how access to data is controlled, especially in collaborative partnerships.
      - Clearly explains
        Who will have access to the data during the research.
      - distribution/data_access
        distribution/licence
      - distribution/restriction_explanation
    * - Consider data protection, particularly if your data is sensitive (for example containing personal data, politically sensitive information, or trade secrets). Describe the main risks and how these will be managed.
      - which institutional and/or national data protection policies are in place and provides a link to where they can be accessed.
      - dataset/security_and_privacy
        dataset/distribution/host/licence
      - distribution/restriction_explanation
        dmp/related_policies
    * - Explain which institutional data protection policies are in place.
      - Clearly describes the additional security measures (in terms of physical security, network security, and security of computer systems and files) that will be taken to ensure that stored and transferred data are safe, when sensitive data are involved (for example personal data, politically sensitive information, or trade secrets).
      - dataset/security_and_privacy
        dataset/distribution/host/licence
      - distribution/restriction_explanation
        dmp/related_policies




Section:  4 LEGAL AND ETHICAL REQUIREMENTS, CODES OF CONDUCT
------------------------------------------------------------

.. list-table:: Subsection: 4a If personal data are processed, how will compliance with legislation on personal data and security be ensured?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Ensure that when dealing with personal data, data protection laws (for example GDPR) are complied with: Gain informed consent for preservation and/or sharing of personal data.
      - Clearly indicates if personal data will be collected/used as part of the project, and, if applicable, how compliance with applicable legislation will be ensured (for example by gaining informed consent, considering encryption, anonymisation, or pseudonymisation).
      - dataset/security_and_privacy
      - distribution/property_rights_explanation

.. list-table:: Subsection: 4b How will other legal issues, such as intellectual property rights and ownership, be managed? What legislation is applicable?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Explain who will be the owner of the data, meaning who will have the rights to control access:
      -
      - contributor/role
      -
    * - Indicate whether intellectual property rights (for example Database Directive, sui generis rights) are affected. If so, explain which and how will they be dealt with.
      -
      -
      - distribution/property_rights_explanation
    * - Indicate whether there are any restrictions on the re-use of third-party data.
      -
      - distribution/data_access
        distribution/licence
      - distribution/restriction_explanation


.. list-table:: Subsection: 4c What ethical issues and codes of conduct are there, and how will they be taken into account?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Consider whether ethical issues can affect how data are stored and transferred, who can see or use them, and how long they are kept. Demonstrate awareness of these aspects and respective planning.
      - Provides details of what ethical issues have been considered that may affect data storage, transfer, use, sharing and/or preservation, and demonstrates that adequate measures are in place to manage ethical requirements.
      - dmp/ethical_issues_exist
        dmp/ethical_issues_description
        dmp/ethical_issues_report
      -
    * - Follow the national and international codes of conducts and institutional ethical guidelines, and check if ethical review (for example by an ethics committee) is required for data collection in the research project.
      - Refers to relevant ethical guidelines and/or codes of conduct or alternatively provides a clear statement that explains why ethical issues have not been considered.
      - dmp/ethical_issues_exist
        dmp/ethical_issues_description
        dmp/ethical_issues_report
      -

Section: 5 DATA SHARING AND LONG-TERM PRESERVATION
--------------------------------------------------

.. list-table:: Subsection: 5a How and when will data be shared? Are there possible restrictions to data sharing or embargo reasons?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Explain how the data will be discoverable and shared (for example by deposit in a trustworthy data repository, indexed in a catalogue, use of a secure data service, direct handling of data requests, or use of another mechanism).
      - Clearly describes how the data and/or metadata will be made discoverable and shared.
      - host/title
        host/url
        distribution/description
        distribution/data_access
      -

.. list-table:: Subsection: 5b How will data for preservation be selected, and where data will be preserved longterm (for example a data repository or archive)?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Indicate what data must be retained or destroyed for contractual, legal, or regulatory purposes.
      - Provides details of what data collected or created in the project will be preserved in the long term and clearly indicates for how long. This should be in alignment with funder, institutional, or national policies and/or legislation, or community standards.
      - dataset/preservation_statement
      - dmp/related_policies
    * - Indicate how it will be decided what data to keep. Describe the data to be preserved long-term.
      - Provides details of which (versions of) data and accompanying documentation will be retained or destroyed, and explains the rationale (for example contractual, legal requirements, or regulatory purposes).
      - dataset/preservation_statement
      -
    * - Explain the foreseeable research uses (and/ or users) for the data.
      - Provides details of how the selection is made, and what possible interest there would be for re-use (or not).
      - dataset/descriptions
      -
    * - Indicate where the data will be deposited. If no established repository is proposed, demonstrate in the data management plan that the data can be curated effectively beyond the lifetime of the grant. It is recommended to demonstrate that the repositories policies and procedures (including any metadata standards, and costs involved) have been checked.
      - Provides details on how the data, accompanying documentation, and any other required technology such as copies of software in specific versions will be archived in the long term.
      - dmp/cost
        dataset/preservation_statement
      -


.. list-table:: Subsection: 5c What methods or software tools are needed to access and use data?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Indicate whether potential users need specific tools to access and (re-)use the data. Consider the sustainability of software needed for accessing the data.
      - Clearly indicates which specific tools or software (for example specific scripts, codes, or algorithms developed during the project, version of the software) potential users may need to access, interpret, and (re-)use the data.
      - dataset/technical_resource
      - dataset/methodology
    * - Indicate whether data will be shared via a repository requests handled directly, or whether another mechanism will be used?
      - Provides information, if relevant, on any protocol to access the data (for example if authentication is needed or if there is a data access request procedure).
      - dataset/dataset_id
      -

.. list-table:: Subsection: 5d How will the application of a unique and persistent identifier (such as a Digital Object Identifier (DOI)) to each data set be ensured?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Explain how the data might be re-used in other contexts. Persistent identifiers (PIDs) should be applied so that data can be reliably and efficiently located and referred to. Persistent identifiers also help to track citations and re-use
      - Specifies how the data can be re-used in other contexts.
        Clearly indicates if and which persistent identifiers (PIDs) are provided for all datasets, individual datasets, data collections, or subsets. If PIDs will not be used, it explains why.
      - dataset/dataset_id
      - dataset/methodology

Section: 6 DATA MANAGEMENT RESPONSIBILITIES AND RESOURCES
---------------------------------------------------------

.. list-table:: Subsection: 6a Who (for example role, position, and institution) will be responsible for data management (i.e. the data steward)?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Outline the roles and responsibilities for data management/ stewardship activities for example data capture, metadata production, data quality, storage and backup, data archiving, and data sharing. Name responsible individual(s) where possible.
      - Clearly outlines the roles and responsibilities for data management/stewardship (for example data capture, metadata production, data quality, storage and backup, data archiving, and data sharing), naming responsible individual(s) where possible.
      - contributor/role
      -
    * - For collaborative projects, explain the co-ordination of data management responsibilities across partners
      - Clearly indicates who is responsible for day-to-day implementation and adjustments to the DMP.
      - contributor/role
      -
    * - Indicate who is responsible for implementing the DMP, and for ensuring it is reviewed and, if necessary, revised.
      - Explains, for collaborative projects, the co-ordination of data management responsibilities across partners.
      - contributor/role
      -
    * - Indicate who is responsible for implementing the DMP, and for ensuring it is reviewed and, if necessary, revised.
      -
      - dmp/modified
      -

.. list-table:: Subsection: 6b What resources (for example financial and time) will be dedicated to data management and ensuring that data will be FAIR (Findable, Accessible,  Interoperable, Reusable)?
    :class: small-table
    :header-rows: 1

    * - Question or Requirement information
      - Evaluation Rubric
      - DCS
      - OSTrails AP
    * - Explain how the necessary resources (for example time) to prepare the data for sharing/preservation (data curation) have been costed in.
      -
      - dmp/cost
      - dataset/methodology
    * - Carefully consider and justify any resources needed to deliver the data. These may include storage costs, hardware, staff time, costs of preparing data for deposit, and repository charges.
      -
      - dmp/cost
      -
    * - Indicate whether additional resources will be needed to prepare data for deposit or to meet any charges from data repositories. If yes, explain how much is needed and how such costs will be covered
      -
      - dmp/cost
        dataset/technical_resource
      -
