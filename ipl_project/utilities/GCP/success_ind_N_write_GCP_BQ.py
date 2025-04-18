def success_ind_N_write_GCP_BQ_fun(df_process_audit_table,
                                    configs.dataset,
                                    configs.process_audit_table,
                                    configs.process_audit_schema):
    gcp_connection.connect_to_bq(df_process_audit_table,
                                    configs.dataset,
                                    configs.process_audit_table,
                                    configs.process_audit_schema)