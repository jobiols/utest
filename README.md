# utest
prueba de test unitarios con estos cambios

En este test.yml debe definirse lo siguiente




1- se debe leer del .copier-answers.yml odoo-version y odoo-edition

segun estas dos variables se baja la imagen necesaria para testear




name: Proceso de GitHub Actions

on:
  push:
    branches:
      - main

jobs:
  procesar_archivo:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout del código
      uses: actions/checkout@v2

    - name: Instalar yq
      run: |
        sudo add-apt-repository ppa:rmescandon/yq -y
        sudo apt-get update -q
        sudo apt-get install yq -y

    - name: Leer .copier-answers.yml
      id: read_yaml
      run: |
        odoo_edition=$(yq r .copier-answers.yml odoo_edition)
        odoo_version=$(yq r .copier-answers.yml odoo_version)
        echo "::set-output name=odoo_edition::${odoo_edition}"
        echo "::set-output name=odoo_version::${odoo_version}"

    - name: Crear nombre de la imagen
      id: nombre_imagen
      run: echo "::set-output name=imagen_name::jobiols/${{ steps.read_yaml.outputs.odoo_version }}-${{ steps.read_yaml.outputs.odoo_edition }}"

  construir_y_ejecutar:
    needs: procesar_archivo
    runs-on: ubuntu-latest

    steps:
    - name: Checkout del código
      uses: actions/checkout@v2

    - name: Construir y descargar la imagen Docker
      run: |
        imagen_name="${{ needs.procesar_archivo.outputs.imagen_name }}"
        docker pull "$imagen_name"

    - name: Install addons and dependencies
      run: oca_install_addons

    - name: Run tests
      run: oca_run_tests
