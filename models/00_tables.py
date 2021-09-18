# -*- coding: utf-8 -*-

"""
    Global tables and re-usable fields
"""

# =============================================================================
# Import models
#
from s3.s3model import S3Model
import s3db as models
current.models = models

# Explicit import statements to have them reload automatically in debug mode
# - still needed when not running debug
import s3db.auth
import s3db.cms
import s3db.doc
import s3db.gis
import s3db.hrm
import s3db.msg
import s3db.org
import s3db.pr
import s3db.s3
import s3db.setup
import s3db.sit
import s3db.sync
import s3db.translate
if debug:
    # Also reload Custom Models
    custom_models = settings.get_base_custom_models()
    for prefix in custom_models:
        parent = __import__("templates.%s" % custom_models[prefix], fromlist=[prefix])

current.s3db = s3db = S3Model()

# =============================================================================
# Configure the auth models
# - needed for admin/user, sync/sync & 1st_run, so could move to a fn called
#   from those 3 if overhead grows
s3db.configure("auth_user",
               # We don't want this for Sync, just in admin/user & 1st_run
               #create_onaccept = lambda form: auth.s3_approve_user(form.vars),
               # @ToDo: Consider moving these pseudo FKs into link tables with real FKs
               references = {"organisation_id": "org_organisation",
                             "site_id": "org_site",
                             "org_group_id": "org_group",
                             },
               )

s3db.add_components("auth_user",
                    auth_membership = "user_id",
                    pr_person_user = "user_id",
                    )

s3db.configure("auth_membership",
               # @ToDo: Consider moving these pseudo FKs into link tables with real FKs
               references = {"pe_id": "pr_pentity",
                             },
               )

# =============================================================================
# Make available for S3Models
# - legacy for backwards compatibility w docs & custom modules
from s3.s3fields import S3ReusableField, s3_comments, s3_meta_fields
s3.comments = s3_comments
s3.meta_fields = s3_meta_fields

# END =========================================================================
