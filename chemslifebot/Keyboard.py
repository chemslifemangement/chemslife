from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#inline buttons for services

serv_key = [
    [
    InlineKeyboardButton("Financial Services", callback_data="finance"),
    InlineKeyboardButton("Tax Services", callback_data="tax")
    ],
    [
    InlineKeyboardButton("Business Services", callback_data="business"),
    InlineKeyboardButton("Educational Services ", callback_data="educ")
    ],
    [
    InlineKeyboardButton("Back", callback_data="close"),
    ]
]
serv_button = InlineKeyboardMarkup(serv_key)

#inline buttons for fiancial services

fin_key =[
    [
    InlineKeyboardButton("Demat Account", callback_data="demat"),
    InlineKeyboardButton("Insurance", callback_data="ins")
    ],
    [
    InlineKeyboardButton("Loan", callback_data="loan"),
    InlineKeyboardButton("Fixed Deposit", callback_data="fdt")
    ],
    [
    InlineKeyboardButton("Portfolio Management ", callback_data="portman"),
    InlineKeyboardButton("Stock SIP", callback_data="stsip"),
    ],
    [
    InlineKeyboardButton("Retirement planning ", callback_data="retireplan"),
    InlineKeyboardButton("Back", callback_data="finanaceback"),
    ]
    
]
fin_button = InlineKeyboardMarkup(fin_key)
#inline button for demat
demat_key = [
    [
    InlineKeyboardButton("New Demat Account", callback_data="nedemat"),
    InlineKeyboardButton("Existing Demat Account ", callback_data="exdemat")
    ],
    [
    InlineKeyboardButton("Back", callback_data="dback")
    ]
]
demat_button = InlineKeyboardMarkup(demat_key)

#inline button for new demat account
new_dematac_key = [
    [
    InlineKeyboardButton("FULL SERVICE BROKING", callback_data="fuser"),
    InlineKeyboardButton("DISCOUNT BROKING", callback_data="disb"),
    ],
    [
    InlineKeyboardButton("Back", callback_data="ndback"),
    ]
]
new_dematac_button = InlineKeyboardMarkup(new_dematac_key)


#inline buttons for tax services

tax_key =[
    [
    InlineKeyboardButton("Income Tax Services", url ="www.chemslife.in"),
    InlineKeyboardButton("GST Services", url ="query@chemslife.in")
    ],
    [
    InlineKeyboardButton("MSME", url ="https://wa.me/919597179325"),
    InlineKeyboardButton("Company Registration", url ="https://t.me/ChemslifeGroups")
    ],
    [
    InlineKeyboardButton("ISO Certification", url ="https://www.youtube.com/c/ChemslifeGroupss"),
    InlineKeyboardButton("TradeMark Registration", url ="https://www.facebook.com/Chemslifegroups"),
    ],
    [
    InlineKeyboardButton("CA Certificates", url ="https://www.youtube.com/c/ChemslifeGroupss"),
    InlineKeyboardButton("Pan Center UTI", callback_data="fback"),
    ],
    [
    InlineKeyboardButton("Back", callback_data="taxback")
    ]
    
]
tax_button = InlineKeyboardMarkup(tax_key)

#inline buttons for business services

busi_key =[
    [
    InlineKeyboardButton("Digital Marketing ", url ="www.chemslife.in"),
    InlineKeyboardButton("Billing and Laboratory Software", url ="query@chemslife.in")
    ],
    [
    InlineKeyboardButton("Website Development", url ="https://wa.me/919597179325"),
    InlineKeyboardButton("Back", callback_data="close")
    ]
    
]
busi_button = InlineKeyboardMarkup(busi_key)

#inline buttons for education services

edu_key =[
    [
    InlineKeyboardButton("Books", url ="www.chemslife.in"),
    InlineKeyboardButton("Webinars", url ="query@chemslife.in")
    ],
    [
    InlineKeyboardButton("Tutorials", url ="https://wa.me/919597179325"),
    InlineKeyboardButton("Research Works", url ="https://t.me/ChemslifeGroups")
    ],
    [
    InlineKeyboardButton("Back", callback_data="close")
    ]
    
]
edu_button = InlineKeyboardMarkup(edu_key)

#inline buttons for membership

Mem_key =[
    [
    InlineKeyboardButton("Account Details", callback_data="accountdetails"),
    InlineKeyboardButton("Pay", url ="query@chemslife.in")
    ],
    [
    InlineKeyboardButton("Back", callback_data="close")
    ]
    
]
Mem_Button = InlineKeyboardMarkup(Mem_key)

#inline buttons for partnership

part_key = [
    [
    InlineKeyboardButton("Products", callback_data="products"),
    InlineKeyboardButton("Services ", callback_data="services")#get to the service list hit service button
    ],
    [
    InlineKeyboardButton("Earning Potential", callback_data="erpotential"),
    InlineKeyboardButton(" Clients", callback_data="clients")
    ],
    [
    InlineKeyboardButton("Benefits", callback_data="accoun"),
    InlineKeyboardButton("Join Now", url ="https://forms.gle/TnwcKraR5f8eqAKh6")
    ],
    [
    InlineKeyboardButton("Back", callback_data="close")
    ]
    
]
part_button = InlineKeyboardMarkup(part_key)


#inline buttons for clients

client_key = [
    [
    InlineKeyboardButton("Services ", callback_data="Cservice"),
    InlineKeyboardButton("Reports",callback_data="reports")
    ],
    [
    InlineKeyboardButton("Call and Trade", callback_data="CaT"),
    InlineKeyboardButton("Help",callback_data= "help")
    ],
    [
    InlineKeyboardButton("Customer Care", callback_data="custom_care"),
    InlineKeyboardButton("Back", callback_data="close")
    ]
]
client_button=InlineKeyboardMarkup(client_key)


#inline buttons for services in clients

client_serv_key = [
    [
    InlineKeyboardButton("Financial Services", callback_data="finance"),
    InlineKeyboardButton("Tax Services", callback_data="tax")
    ],
    [
    InlineKeyboardButton("Business Services", callback_data="business"),
    InlineKeyboardButton("Educational Services ", callback_data="educ")
    ],
    [
    InlineKeyboardButton("Back", callback_data="cback"),
    ]
]
client_serv_button = InlineKeyboardMarkup(client_serv_key)
 
#inline buttons for reports in clients

client_report_key = [
    [
    InlineKeyboardButton("Research Reports ", url = "https://t.me/ChemslifeGroups"),
    InlineKeyboardButton("Accounts", callback_data=" ")
    ],
    [
    InlineKeyboardButton("Back", callback_data="cback"),
    ]
]
client_report_button = InlineKeyboardMarkup(client_report_key)

#inline buttons for help in clients

client_help_key = [
    [
    InlineKeyboardButton("Trading issues ", callback_data="accoun"),
    InlineKeyboardButton("Software / App Issues ", url ="query@chemslife.in")
    ],
    [
    InlineKeyboardButton("Need Trainning", callback_data="aback"),
    InlineKeyboardButton("others", url ="query@chemslife.in")
    ],
    [
    InlineKeyboardButton("Back", callback_data="cback")
    ]
]

client_help_button = InlineKeyboardMarkup(client_help_key)  

#inline button for reports
accoun_report_key = [
    [
    InlineKeyboardButton("Combined Ledger ", url ="www.chemslife.in"),
    InlineKeyboardButton("Holding Report", url ="query@chemslife.in")
    ],
    [
    InlineKeyboardButton("FNO P&L Report", url ="https://wa.me/919597179325"),
    InlineKeyboardButton(" Dividend", url ="https://t.me/ChemslifeGroups")
    ],
    [
    InlineKeyboardButton("DP Transaction cum Holding", url ="https://www.youtube.com/c/ChemslifeGroupss"),
    InlineKeyboardButton("Fund Transaction Report", url ="https://www.facebook.com/Chemslifegroups"),
    ],
    [
    InlineKeyboardButton("NBFC Ledger", url ="https://twitter.com/ChemslifeGroups"),
    InlineKeyboardButton("NSE Currency P&L Report ", url ="https://www.instagram.com/chemslife_groups/")
    ],
    [
    InlineKeyboardButton("COMM. Client Ledger ", url ="https://www.linkedin.com/in/chemslife-groups-278a10213/"),
    InlineKeyboardButton("FNO Ledger", url ="https://g.page/chemslife")
    ],
    [
    InlineKeyboardButton("Equity P&L Statement", url ="https://www.linkedin.com/in/chemslife-groups-278a10213/"),
    InlineKeyboardButton("Pool Holding Summary", url ="https://g.page/chemslife")
    ],
    [
    InlineKeyboardButton("Trade Report Detail - Datawise ", url ="https://www.linkedin.com/in/chemslife-groups-278a10213/"),
    InlineKeyboardButton("Trade Report Detail  - Scriptwise", url ="https://g.page/chemslife")
    ],
    [
    InlineKeyboardButton("Trade Report Summary - Datawise ", url ="https://www.linkedin.com/in/chemslife-groups-278a10213/"),
    InlineKeyboardButton("Trade Report Summary - Scriptwise", url ="https://g.page/chemslife")
    ],
    [
    InlineKeyboardButton("BSE STT Statement", url ="https://www.linkedin.com/in/chemslife-groups-278a10213/"),
    InlineKeyboardButton("NSE STT Statement", url ="https://g.page/chemslife")
    ],
    [
    InlineKeyboardButton("NSEFNO STT Statement", url ="https://www.linkedin.com/in/chemslife-groups-278a10213/"),
    InlineKeyboardButton("Client Master List", url ="https://g.page/chemslife")
    ],
    [
    InlineKeyboardButton("Contract Notes", url ="https://www.linkedin.com/in/chemslife-groups-278a10213/"),
    InlineKeyboardButton("MF Portfolio Statement", url ="https://g.page/chemslife")
    ],
    [
    InlineKeyboardButton("All Segment P&L", url ="https://g.page/chemslife"),
    InlineKeyboardButton("Back", callback_data="rback"),
    ]
]

accoun_report_button = InlineKeyboardMarkup(accoun_report_key)


#inline buttons for contacts

contact_keyboard =[
    [
    InlineKeyboardButton("Website", url ="www.chemslife.in"),
    InlineKeyboardButton("Mail", url ="query@chemslife.in")
    ],
    [
    InlineKeyboardButton("Whatsapp", url ="https://wa.me/919597179325"),
    InlineKeyboardButton(" Telegram channel", url ="https://t.me/ChemslifeGroups")
    ],
    [
    InlineKeyboardButton("Youtube ", url ="https://www.youtube.com/c/ChemslifeGroupss"),
    InlineKeyboardButton("Facebook", url ="https://www.facebook.com/Chemslifegroups"),
    ],
    [
    InlineKeyboardButton("Twitter", url ="https://twitter.com/ChemslifeGroups"),
    InlineKeyboardButton("Instagram", url ="https://www.instagram.com/chemslife_groups/")
    ],
    [
    InlineKeyboardButton("Linked In", url ="https://www.linkedin.com/in/chemslife-groups-278a10213/"),
    InlineKeyboardButton("Google Business", url ="https://g.page/chemslife")
    ],
    [
    InlineKeyboardButton("Back", callback_data="close"),
    ]
]
Contact_button = InlineKeyboardMarkup(contact_keyboard)