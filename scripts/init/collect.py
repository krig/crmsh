#!/usr/bin/env python3
import crm_script
import crm_init
try:
    crm_script.exit_ok(crm_init.info())
except Exception as e:
    crm_script.exit_fail(str(e))
