#!/bin/sh
# #####################################################################################
# Generar base de test con datos de prueba y opcionalmente instalarle módulos a testear
#
# Este script requiere en la carpeta backup_dir una subcarpeta bkp_test en la que debe
# haber un backup llamado test.zip que contiene un backup de una base vacia con datos
# de prueba credenciales admin / admin y sin modificar pais y lenguaje de los valores
# por defecto.
# #####################################################################################

IMAGE="jobiols/odoo-jeo:16.0.debug"
DB="pg-utest:db"
BASE=$(readlink -f "../../..")

# restaurar la base de test vacia
cp $BASE/utest/backup_dir/bkp_test/test.zip $BASE/utest/backup_dir/
oe --restore -d utest_test --no-deactivate -f test.zip
rm $BASE/utest/backup_dir/test.zip

sudo docker run --rm -it \
    --link wdb \
    --link $DB \
    -v $BASE/utest/config:/opt/odoo/etc/ \
    -v $BASE/utest/data_dir:/opt/odoo/data \
    -v $BASE/utest/log:/var/log/odoo \
    -v $BASE/utest/sources:/opt/odoo/custom-addons \
    -v $BASE/utest/backup_dir:/var/odoo/backups/ \
    -v $BASE/extra-addons:/opt/odoo/extra-addons \
    -v $BASE/dist-packages:/usr/lib/python3/dist-packages \
    -v $BASE/dist-local-packages:/usr/local/lib/python3.9/dist-packages \
    -e ODOO_CONF=/dev/null \
    -e WDB_SOCKET_SERVER=wdb $IMAGE --stop-after-init -d utest_test \
    -i modulo-a-testear # --test-enable.
