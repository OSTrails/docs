Austrian FWF – maDMP mapping
===============================================

We performed a mapping for each section using te Evaluation Rubric of the FWF template.

Section:  I General Information
---------------------------------

.. list-table:: Subsection: I.1 Administrative information
   :class: small-table
   :header-rows: 1

   * - Question or Requirement information
     - Evaluation Rubric
     - DCS
     - OSTrails AP
   * - Provide information such as name of principal investigator, FWF project number, and version of DMP
     - Contains the minimal information required to identify the principal investigator and the references of the project as well as the version of the DMP.
     - dmp/contact/name, 
       dmp/project/number, 
       dmp/project/description,
       dmp/project/funding/funder_id,
       dmp/project/funding/grant_id,
     -  

.. list-table:: Subsection: I.2 Data management responsibilities and resources
   :class: small-table
   :header-rows: 1

   * - Question or Requirement information
     - Evaluation Rubric
     - DCS
     - OSTrails AP
   * - Who (for example, role, position, and institution) will be responsible for data management?
     - Clearly outlines the roles and responsibilities for data management, naming responsible individual(s) and clearly indicates who is responsible for day-to-day implementation and adjustments to the DMP.
     - contributor/contributor_id,
       contributor/role,
       contributor/affiliation,
       contributor/name,
     -  
   * - What resources will be dedicated to data management and ensuring that data will be FAIR (Findable, Accessible, Interoperable, Re-usable)?
     - Provides clear estimates of the resources and costs (for example, staff time and repository charges) that will be dedicated to data management and ensuring that data will be FAIR and describes how these costs will be covered. Alternatively, there is a statement that no additional resources are needed.
     - cost/description,
       cost/value, 
       cost/title,
     - 

Section:  II Data Characteristics
---------------------------------

.. list-table:: Subsection: II.1 Data description and collection or re-use of existing data
   :class: small-table
   :header-rows: 1

   * - Question or Requirement information
     - Evaluation Rubric
     - DCS
     - OSTrails AP
   * - How will new data be collected or produced and/or how will existing data be re-used?
     - Gives clear details of where the existing data come from and how new data will be collected or produced. It clearly explains methods and software used.
     - 
     - dataset/methodology
   * - What data (types, formats, and, volumes) will be collected or produced?
     - Explains, if existing data are re-used, how these data will be accessed and any constraints on their re-use.
     - dataset/is_reused, 
       dataset/distribution
       /data_access,
     -
   * - 
     - Clearly describes or lists what data types will be generated (for example, numeric, textual, audio, or video) and their associated data formats.
     - dataset/type ,
       dataset/distribution
       /format
     - 
   * - 
     - Explains why certain formats have been chosen and indicates if they are in open and standard format. If a proprietary format is used, it explains why.
     - dataset/distribution
       /description,
     - dataset/distribution
       /format_justification
   * - 
     - Provides information about the estimated data volume.
     - dataset/distribution/byte_size
     - 


Section:  III Documentation and Data Quality
------------------------------------------------

.. list-table:: Subsection: III.1 Metadata and documentation
   :class: small-table
   :header-rows: 1

   * - Question or Requirement information
     - Evaluation Rubric
     - DCS
     - OSTrails AP
   * - What metadata and documentation (for example, the methodology of data collection and way of organising the data) will accompany the data?
     - Clearly outlines the metadata that will accompany the data, with reference to good practice in the community (for example, uses metadata standards where they exist).
     - datset/metadata
     - 
   * - 
     - Indicates how the data will be organised during the project (for example, naming conventions, version control strategy, and folder structures).
     - dataset/metadata
       dataset/data_quality_assurance
     - 
   * - 
     - Clearly outlines the documentation needed to enable data re-use, stating where the information will be recorded (for example, a database with links to each item, a ‘readme’ text file, code books, or lab notebooks).
     - 
     - dataset/methodology

.. list-table:: Subsection: III.2 Data quality control
   :class: small-table
   :header-rows: 1

   * - Question or Requirement information
     - Evaluation Rubric
     - DCS
     - OSTrails AP
   * - What data quality control measures will be used?
     - Clearly describes the approach taken to ensure and document quality control in the collection of data during the lifetime of the project.
     - 
     - dataset/methodology

Section:  IV Data Storage, Sharing, and Long-Term Preservation
--------------------------------------------------------------------

.. list-table:: Subsection: IV.1 Data storage and backup during the research process
   :class: small-table
   :header-rows: 1

   * - Question or Requirement information
     - Evaluation Rubric
     - DCS
     - OSTrails AP
   * - How will the data and metadata be stored and backed up during the research process?
     - The location where the data and backups will be stored during the research activities.
     - dataset/distribution
       /host/url
     - 
   * - 
     - How often backups will be performed.
     - dataset/distribution
       /host/backup_type
     - 
   * - 
     - The use of robust, managed storage with automatic backup (for example, storage provided by the home institution).
     - dataset/distribution
       /host/backup_frequency,
       dataset/distribution
       /host/backup_type
     - 
   * - 
     - Explains why institutional storage will not be used (and for what part of the data) and describes the (additional) locations, storage media, and procedures that will be used for storing and backing up data during the project.
     - dataset/distribution
       /host/description,
       dataset/distributions
       /host/url ,
       dataset/distribution
       /access_url
     - 
   * - How will data security and protection of sensitive data be taken care of during the research?
     - How the data will be recovered in the event of a technical incident.
     - dataset/distribution
       /host/title,
       dataset/distribution
       /host/description,
     - dataset/distribution
       /host/recovery_plan

.. list-table:: Subsection: IV.2 Data sharing and long-term preservation
   :class: small-table
   :header-rows: 1

   * - Question or Requirement information
     - Evaluation Rubric
     - DCS
     - OSTrails AP
   * - How and when will the data be shared? Are there restrictions to data sharing or embargo reasons?
     - Clearly describes how and when the data will be made discoverable and shared.
     - dataset/distroibution/*,
       dataset/distributions/host/*,
       dataset/distribution
       /license/start_date,
       dataset/issued
     - 
   * - In which repository will the data be archived and made available for re-use? What persistent identifier (e.g., DOI) and which usage licence (e.g., CC BY) will be used?
     - Specifies a repository for data re-use and explains which persistent identifiers (PIDs) are provided for the data and under which licence the data will be made available. (see FWF Open Access Policy for Research Data).
     - dataset/distribution
       /host/url,
       dataset/distribution
       /licenselicense_ref
     - 
   * - 
     - Clearly explains, if applicable, why data sharing is limited or not possible, and who can access the data under which conditions (for example, only members of certain communities or via a sharing agreement).
     - dataset/security_and _privacy,
       dataset/personal_data,
       dataset/sensitive_data
     - 
   * - 
     - Explains what actions will be taken to overcome or to minimise data sharing restrictions.
     - dataset/distribution
       /license/start_date
     - 
   * - What methods and software tools are needed to access and use the data?
     - Clearly indicates which specific tools or software (for example, specific scripts, codes, or algorithms developed during the project, version of the software) potential users may need to access, interpret, and (re-) use the data.
     - dataset/technical_resouce/*
     -
   * - 
     - Provides details on how the data, accompanying documentation, and any other required technology such as copies of software in specific versions will be archived in the long term.
     - dataset/distribution/host/url
     - 
   * - How will data for preservation be selected, and where will the data be preserved long-term?
     - Provides details of which (versions of) data and accompanying documentation will be retained or destroyed, and explains the rationale (for example, contractual, legal requirements, or regulatory purposes).
     - dataset/preservation_statement
     - dmp/related_policy
   * - 
     - Provides details of what data collected or created in the project will be preserved in the long term and clearly indicates for how long. This should be in alignment with institutional, or national policies and/or legislation, or community standards.
     - dataset/preservation_statement,
       dataset/distribution
       /license/start_date,
       dataset/data_quality_assurance
     - 



Section:  V Legal and Ethical Aspects
--------------------------------------------------------------------

.. list-table:: Subsection: V.1 Legal aspects
   :class: small-table
   :header-rows: 1

   * - Question or Requirement information
     - Evaluation Rubric
     - DCS
     - OSTrails AP
   * - How will legal issues, such as intellectual property rights and ownership, be managed? What legislation is applicable?
     - Clearly explains who will have the rights to control access to the data.
     - dataset/creator/*,
       dataset/distribution
       /license/license_ref,
       dataset/data_quality_assurance
     - 
   * - 
     - Explains for multi-partner projects and multiple data owners how these matters are addressed in the consortium agreement.
     - dataset/distribution
       /license/license_ref,
       dataset/data_quality_assurance
     - 
   * - 
     - Clearly explains, if applicable, how intellectual property rights will be managed.
     - 
     - dataset/distribution
       /property_rights_explanation
   * - 
     - Indicates, if applicable, whether there are any restrictions on the re-use of third-party data.
     - 
     - dataset/distribution
       /restriction_explanation
   * - If personal data are processed, how will compliance with legislation on personal data and on security be ensured?
     - Clearly indicates if personal data will be collected/used as part of the project, and, if applicable, how compliance with applicable legislation will be ensured (for example, by gaining informed consent, considering encryption, anonymisation, or pseudonymisation).
     - dataset/personal_data
     - 

.. list-table:: Subsection: V.2 Ethical aspects
   :class: small-table
   :header-rows: 1

   * - Question or Requirement information
     - Evaluation Rubric
     - DCS
     - OSTrails AP
   * - What ethical issues and codes of conduct are there, and how will they be taken into account?
     - Provides details of what ethical issues have been considered that may affect data storage, sharing, and/or preservation, and demonstrates that adequate measures are in place to manage ethical requirements.
     - dataset/security_and_privacy
     - 
   * - 
     - Mentions, if applicable, whether ethical review is being pursued. If ethical approval has been obtained, refers to the relevant committee and documents.
     - ethical_issues_exist,
       ethical_issues_report,
       ethical_issues_description
     - 
   * - 
     - Refers to relevant ethical guidelines and/or codes of conduct or alternatively provides a clear statement that explains why ethical issues have not been considered.
     - 
     - dmp/related_policy
