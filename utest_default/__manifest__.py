##############################################################################
#
#    Copyright (C) 2021  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "utest",
    "version": "16.0.1.0.0",
    "category": "Tools",
    "author": "Quilsoft",
    "summary": "Test for v16 EE",
    "license": "AGPL-3",
    "depends": [],
    "data": [],
    "installable": True,
    "application": True,
    "config": [
        # 'addons_path' is always computed looking for the repositories in sources
        # 'data_dir' is a fixed location inside docker odoo image
        # You should use 2 worker threads + 1 cron thread per available CPU,
        # and 1 CPU per 10 concurent users.
        # if ommited oe will calculate workers and cron´s based on # of cpu
        "workers = 0",
        "max_cron_threads = 1",
        # Number of requests a worker will process before being recycled and
        # restarted. Defaults to 8192 if ommited
        "limit_request = 8192",
        # Maximum allowed virtual memory per worker. If the limit is exceeded,
        # the worker is killed and recycled at the end of the current request.
        # Defaults to 640MB
        "limit_memory_soft = 2147483648",
        # Hard limit on virtual memory, any worker exceeding the limit will be
        # immediately killed without waiting for the end of the current request
        # processing. Defaults to 768MB.
        "limit_memory_hard = 2684354560",
    ],
    # Here begins odoo-env manifest configuration
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # manifest version, if omitted it is backward compatible
    "env-ver": "2",
    # if Enterprise it installs in a different directory than community
    "odoo-license": "CE",
    # port where odoo starts serving pages
    "port": "8069",
    # list of url repos to install in the form 'repo-url directory'
    "git-repos": [
        "git@github.com:siseservicios/utest.git",
    ],
    # list of images to use in the form 'name image-url'
    "docker-images": [
        "odoo jobiols/odoo-ent:16.0e",
        "postgres postgres:15.1-alpine",
    ],
}
