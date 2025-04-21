# Pipeline de Distribuição no Databricks

Este projeto realiza a ingestão, tratamento e agregações dos dados de distribuição de equipamentos médicos utilizando o Databricks sobre infraestrutura AWS.

## Etapas

1. Ingestão com Auto Loader (camada Bronze)
2. Tratamento dos dados (camada Silver)
3. Agregações por UF e tipo de equipamento (camada Gold)
4. Orquestração com Databricks Workflows

## Como usar

1. Suba os dados no bucket S3: `/mnt/raw/distribuicao`
2. Execute os notebooks na ordem 01 → 02 → 03
3. Agende com Databricks Workflows utilizando o arquivo `pipeline_job.json`