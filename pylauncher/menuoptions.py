"""
Fill in this list of lists / tuple of tuples with the options needed 
for your launcher menu using the following format: 

('Displays in menu', 'RepoFolderName', 'src/myscript.py', 'EnvironmentFolder'),

NOTE: Use None value if your repo doesn't use a virtual environment folder.
"""


OPS = (

    ('Counter Calculator', 'PrintShopScripts', 'scripts/counter_calculator.py', None),
    ('Booklet Estimate', 'PrintShopScripts', 'scripts/booklet_estimate.py', None),
    ('Subset Finishing', 'PrintShopScripts', 'scripts/subset_finishing.py', None),
    ('Materals By Set Calculator', 'PrintShopScripts', 'scripts/materials_calculator.py', None),
    ('Ticket Numbering Assist', 'PrintShopScripts', 'scripts/ticket_numbering.py', None),
    ('VBS Calculator', 'PrintShopScripts', 'scripts/vbs_calculator.py', None),
    ('Mail Logs Calculator', 'PrintShopScripts', 'scripts/mail_logs_calculator.py', None),
    ('Generate MS Invoice Details', 'MSInvoiceDetails', 'msinvoice', 'env'),
    ('Get Papercut Reports', 'get-papercut-reports', 'getreports/get_papercut_reports.py', 'env'),
    ('Generate PaperCut Packages', 'papercut-sw-packager', 'pcswpkgr/papercut_sw_packager.py', 'env'),
    ('Compile MOR', 'CompileMOR', 'compmor/compile_mor.py', 'env'),

    # Leave this one last for an exit option
    ('Exit', 'EXIT', '', None)

)
