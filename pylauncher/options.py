"""
Fill in this list of lists / tuple of tuples with the options needed 
for your launcher menu using the following format: 

('Displays in menu', 'RepoFolderName', 'src/myscript.py', 'EnvironmentFolder'),

NOTE: Use None value if your repo doesn't use a virtual environment folder.
"""


PSP = (

    ('Counter Calculator', 'PrintShopScripts', 'scripts/counter_calculator.py', None),
    ('Booklet Estimate', 'PrintShopScripts', 'scripts/booklet_estimate.py', None),
    ('Subset Finishing', 'PrintShopScripts', 'scripts/subset_finishing.py', None),
    ('Materals By Set Calculator', 'PrintShopScripts', 'scripts/materials_calculator.py', None),
    ('Ticket Numbering Assist', 'PrintShopScripts', 'scripts/ticket_numbering.py', None),
    ('VBS Calculator', 'PrintShopScripts', 'scripts/vbs_calculator.py', None),
    ('Mail Logs Calculator', 'PrintShopScripts', 'scripts/mail_logs_calculator.py', None),
    ('Count Files in Directory', 'CountFiles', 'countfiles', None),

    ('[ Back ]', 'BACK', '', None),
    ('[ Exit ]', 'EXIT', '', None)

)

SSP = (

    ('Generate Department Charges', 'DeptCharges', 'deptcharges', 'env'),
    ('Check Charges for Missing Tickets', 'CheckMissingTickets', 'checktickets', 'env'),
    ('Generate MS Invoice Details', 'MSInvoiceDetails', 'msinvoice', 'env'),
    ('Generate TS Invoice Details', 'TSInvoiceDetails', 'tsinvoice', 'env'),
    ('Process Meter Reads', 'GetMeters', 'getmeters', 'env'),
    ('Compile MOR', 'CompileMOR', 'compmor', 'env'),

    ('[ Back ]', 'BACK', '', None),
    ('[ Exit ]', 'EXIT', '', None)

)

MDS = (

    ('Get Papercut Reports', 'GetPapercutReports', 'getreports/get_papercut_reports.py', 'env'),
    ('Generate PaperCut Packages', 'PapercutSWPackager', 'pcswpkgr/papercut_sw_packager.py', 'env'),

    ('[ Back ]', 'BACK', '', None),
    ('[ Exit ]', 'EXIT', '', None)

)