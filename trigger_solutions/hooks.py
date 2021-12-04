from . import __version__ as app_version

from frappe import _

app_name = "trigger_solutions"
app_title = "Trigger Solutions"
app_publisher = "Trigger Solutions pvt. ltd."
app_description = "ERP UI made simple"
app_icon = "fa fa-th"
app_color = "#e74c3c"
app_email = "trigger.solutions.eg@gmail.com"
app_license = "Trigger Solutions General Private License"
app_logo_url = "/assets/trigger_solutions/images/Trigger-Solutions-Logo.png"


website_context = {
	"favicon": 	"/assets/trigger_solutions/images/Trigger-Solutions-Logo.png",
	"splash_image": "/assets/trigger_solutions/images/Trigger-Solutions-Logo.png"
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/trigger_solutions/css/trigger_solutions.css"
# app_include_js = "/assets/trigger_solutions/js/trigger_solutions.js"

# include js, css files in header of web template
# web_include_css = "/assets/trigger_solutions/css/trigger_solutions.css"
# web_include_js = "/assets/trigger_solutions/js/trigger_solutions.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "trigger_solutions/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "trigger_solutions.install.before_install"
# after_install = "trigger_solutions.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "trigger_solutions.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"trigger_solutions.tasks.all"
# 	],
# 	"daily": [
# 		"trigger_solutions.tasks.daily"
# 	],
# 	"hourly": [
# 		"trigger_solutions.tasks.hourly"
# 	],
# 	"weekly": [
# 		"trigger_solutions.tasks.weekly"
# 	]
# 	"monthly": [
# 		"trigger_solutions.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "trigger_solutions.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "trigger_solutions.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "trigger_solutions.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"trigger_solutions.auth.validate"
# ]

