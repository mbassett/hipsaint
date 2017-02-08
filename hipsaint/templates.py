"""
Templates used to build hipchat api payloads
"""

host_template = """
<strong>{hostname} {hostalias}  (icinga@{nagios_host})</strong><br/>
<strong>Type:</strong> {ntype}<br/>
<strong>Host:</strong> <a href="https://{nagios_host}/icingaweb2/monitoring/host/show?host={hostname}">{hostalias} ({hostname})</a><br/>
<strong>State:</strong> HOST {state}<br>
<strong>Info:</strong>
<pre>{hostoutput}</pre>"""

if """{notificationcomment}""" != "":
    host_template += "<p>{notificationcomment}<br>&nbsp;&nbsp;-{notificationauthor}</p>"


host_medium_template = "<strong>{timestamp} - {hostname} ({hostaddress}) - {ntype}/{state}</strong><br/><pre>{hostoutput}</pre>"
host_short_template = """[{ntype}] {hostname}: {hostoutput}"""

service_template = """
<strong>{servicedesc} on {hostalias} (icinga@{nagios_host})</strong><br/>
<strong>Type:</strong> {ntype}<br/>
<strong>Host:</strong> <a href="https://{nagios_host}/icingaweb2/monitoring/service/show?host={hostname}&service={servicedesc}">{hostalias} ({hostname}) {servicedesc}</a>
<strong>State:</strong> SERVICE {state}<br/>
<strong>Info:</strong>
<pre>{serviceoutput}</pre>
"""

if """{notificationcomment}""" != "":
    service_template += "<p>{notificationcomment}<br>&nbsp;&nbsp;-{notificationauthor}</p>"


service_medium_template = "<strong>{timestamp} - {servicedesc} on {hostalias} ({hostaddress}) - {ntype}/{state}</strong><br/><pre>{serviceoutput}</pre>"
service_short_template = "[{ntype}] {hostalias} {servicedesc}: {serviceoutput}"


templates = {'host': host_template, 'medium-host': host_medium_template, 'short-host': host_short_template,
             'service': service_template, 'medium-service': service_medium_template, 'short-service': service_short_template}
