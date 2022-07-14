import tgcrypto
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from text import (
    contacts, 
    Feedback ,
    com_text, 
    Member_msg, 
    Accoun_msg, 
    client_help_msg, 
    client_custom_care, 
    client_msg, 
    part_msg, 
    cat_msg,
    demat_account,
    new_demat_account,
    discount_brok_msg,
    exit_demat_msg,
    full_service_msg
    )
from Keyboard import (
    Contact_button, 
    serv_button, 
    fin_button,
    demat_button,
    new_dematac_button, 
    busi_button,
    edu_button,
    tax_button, 
    Mem_Button,
    client_help_button, 
    client_button,
    client_serv_button,
    client_report_button, 
    accoun_report_button,
    part_button
)


chemi = Client(
    "chemslifebot",
    api_id= "",
    api_hash="",
    bot_token=""
)

button = [
    [ "Services", "Membership"],
    ["Clients", "Partnership Program"],
    ["Contacts", "Feedback"]
    
    ]
START_MSG ="""
Hi {}
WELCOME to **Chemslife Groups**
we are providing the best services in below \n** * Financical Service**, \n** * Tax managmentServices**, \n** * EducationalServices**,\n** * Business Solutions**\n\n You can get details by clicking the buttons below 
"""


@chemi.on_message(filters.command('start') & filters.private)
async def starti(bot:chemi,message):
 
    await message.reply_text(
        text = START_MSG.format(message.from_user.mention),
        reply_markup = ReplyKeyboardMarkup(button, one_time_keyboard=True, resize_keyboard=True)
    )

@chemi.on_message(filters.regex("Services"))
async def serv_com(bot,message):

    await message.reply_text(
        text = com_text,
        reply_markup = serv_button
    )
@chemi.on_message(filters.regex("Membership"))
async def mem_com(bot,message):
    user = message.from_user.mention

    await message.reply_text(
        text = Member_msg.format(user),
        reply_markup = Mem_Button
    )
@chemi.on_message(filters.regex("Clients"))
async def client_com(bot,message):
    await message.reply_text(
        text = client_msg.format(message.from_user.mention),
        reply_markup = client_button
    )
@chemi.on_message(filters.regex("Partnership Program"))
async def part_com(bot,message):
    

    await message.reply_text(
        text = part_msg.format(message.from_user.mention),
        reply_markup = part_button
    )

@chemi.on_message(filters.regex("Contacts"))
async def con_com(bot,message):
    await message.reply_text(
        text =contacts,
        reply_markup = Contact_button
    )


@chemi.on_message(filters.regex("Feedback"))
async def feed_com(bot,message):
    await message.reply_text(text = Feedback)


@chemi.on_callback_query()
async def callback(bot, msg:CallbackQuery):
    mention = msg.from_user.mention

    if msg.data == "finance": #callbackquery for financial services
        await msg.edit_message_text(
            text= com_text,
            reply_markup= fin_button

        )
    elif msg.data == "tax": #callbackqiery for taxservices
        await msg.edit_message_text(
            text= com_text,
            reply_markup= tax_button

        )
    elif msg.data == "business": #callback query for business services
        await msg.edit_message_text(
            text= com_text,
            reply_markup= busi_button

        )
    elif msg.data == "educ": # callbackquery for educational services
        await msg.edit_message_text(
            text= com_text,
            reply_markup= edu_button

        )
    elif msg.data == "demat": #callback query for demat account
        await msg.edit_message_text(
            text= demat_account,
            reply_markup= demat_button

        )
    elif msg.data == "nedemat":#callbaclquery for new demat account
        await msg.edit_message_text(
            text= new_demat_account,
            reply_markup= new_dematac_button,
            disable_web_page_preview=True

        )
    elif msg.data == "exdemat": #callbackquery for existing demat account
        await msg.edit_message_text(
            text=exit_demat_msg,
            reply_markup= InlineKeyboardMarkup(
                [
                [InlineKeyboardButton("BACK", callback_data="exdback")]
                ]
            ),
            disable_web_page_preview=True

        )
    elif msg.data == "fuser": #callbackquery for fullservice broking
        await msg.edit_message_text(
            text= full_service_msg,
            reply_markup= InlineKeyboardMarkup(
                [
                [InlineKeyboardButton("BACK", callback_data="fuserback")]
                ]
            ),
            disable_web_page_preview=True

        )
    elif msg.data == "disb": #callback query for discount broking
        await msg.edit_message_text(
            text= discount_brok_msg,
            reply_markup= InlineKeyboardMarkup(
                [
                [InlineKeyboardButton("BACK", callback_data="disback")]
                ]
            ),
            disable_web_page_preview=True

        )
    
    elif msg.data == "Cservice":
        await msg.edit_message_text(
            text= com_text,
            reply_markup= client_serv_button

        )
    elif msg.data == "reports":
        await msg.edit_message_text(
            text= "Welcome to the report section",
            reply_markup= client_report_button

        )
    elif msg.data == "CaT":
        await msg.edit_message_text(
            text= cat_msg,
            reply_markup= InlineKeyboardMarkup(
                [
                [InlineKeyboardButton("BACK", callback_data="catback")]
                ]
            ),


        )
    elif msg.data == "help":
        await msg.edit_message_text(
            text= client_help_msg,
            reply_markup= client_help_button

        )

    elif msg.data == "custom_care":
        await msg.edit_message_text(
            text= client_custom_care,

            reply_markup= InlineKeyboardMarkup(
                [
                [InlineKeyboardButton("BACK", callback_data="customback")]
                ]
            ),


        )
    elif msg.data == "accounts":
        await msg.edit_message_text(
            text= "Please press below button to gemerate your report",
            reply_markup= accoun_report_button

        )
    elif msg.data == "finanaceback" or "taxback" or "Busiback" or "eduback" or "memback" or "partback" :
        await msg.edit_message_text(
            text= com_text,
            reply_markup= serv_button

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= com_text,
            reply_markup= serv_button

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= com_text,
            reply_markup= serv_button

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= com_text,
            reply_markup= serv_button

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= com_text,
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    elif msg.data == "":
        await msg.edit_message_text(
            text= "",
            reply_markup= ""

        )
    
    elif msg.data == "accountdetails": #membership account details
        await msg.edit_message_text(
            text= Accoun_msg,
            reply_markup=InlineKeyboardMarkup(
                [
                [InlineKeyboardButton("BACK", callback_data="accback")]
                ]
            ),

        )

    elif msg.data == "close":

       await msg.message.delete()
       
       await msg.message.reply_text("Thank you for choosing us")

        


    


print("alive")
chemi.run()

"""
elif msg.data == "mem":
        await msg.message.edit(
            text=com_text,
            reply_markup = fin_button
        
        )
        elif msg.data == "resreport":
        button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Researchreport")
                ]
            ]
        )
        await msg.edit_message_text(
            text=client_msg.format(mention),
            reply_markup = client_button
        )
        elif msg.data == "csaback":
        await msg.edit_message_text(
            text=client_msg.format(mention),
            reply_markup = client_button
        )
    elif msg.data == "csaback":
        await msg.edit_message_text(
            text=client_msg.format(mention),
            reply_markup = client_button
        )
    elif msg.data == "csaback":
        await msg.edit_message_text(
            text=client_msg.format(mention),
            reply_markup = client_button
        )
    elif msg.data == "csaback":
        await msg.edit_message_text(
            text=client_msg.format(mention),
            reply_markup = client_button
        )
    elif msg.data == "csaback":
        await msg.edit_message_text(
            text=client_msg.format(mention),
            reply_markup = client_button
        )


    if msg.data == "finance":
        await msg.edit_message_text(
            text=com_text,
            reply_markup = fin_button
        )
#demat account callback query  
    elif msg.data == "demat":
        
        await msg.edit_message_text(
            text=demat_account,
            reply_markup = demat_button
        
        )
#new demat account callback query   
    elif msg.data == "nedemat":
        await msg.edit_message_text(
            text=new_demat_account,
            reply_markup = new_dematac_button
        
        )
#exiting demat account callback query     
    elif msg.data == "exdemat":
        await msg.edit_message_text(
            text=exit_demat_msg,
            reply_markup = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Back", callback_data="exback")]
    ]
    )
        
        )
# full service demat account callback query      
    elif msg.data == "fuser":
        await msg.edit_message_text(
            text=full_service_msg,
            reply_markup =InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Back", callback_data="fusback")]
    ]
    )
        
        )
#discount broking demat account callback query     
    elif msg.data == "disb":
        await msg.edit_message_text(
            text=discount_brok_msg,
            reply_markup = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Back", callback_data="fusback")]
    ]
    )
        
    )
    elif msg.data == "fusback":
        await msg.edit_message_text(
            text=new_demat_account,
            reply_markup = new_dematac_button
        
        )
    elif msg.data == "dback":
        await msg.edit_message_text(
            text=com_text,
            reply_markup = fin_button
        
        )
    elif msg.data == "exback" or "ndback":
        await msg.edit_message_text(
            text=demat_account,
            reply_markup = demat_button
        
        )
    
    elif msg.data == "tax":
        await msg.edit_message_text(
            text=com_text,
            reply_markup = tax_button
        )
    elif msg.data == "business":
        await msg.edit_message_text(
            text=com_text,
            reply_markup = busi_button
        )
    elif msg.data == "educ":
        await msg.edit_message_text(
            text=com_text,
            reply_markup = edu_button
        )
    elif msg.data == "help":
        await msg.edit_message_text(
            text=client_help_msg,
            reply_markup = client_help_button
        )
    elif msg.data == "custom_care":
        
        await msg.edit_message_text(
            text=client_custom_care, 
            reply_markup = InlineKeyboardMarkup(
                [
                [InlineKeyboardButton("Back", callback_data="cback")]
                ]
            )
        )
    
    elif msg.data == "CaT":
        keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Back", callback_data="cback") 
        ]
    ]
    )
        await msg.message.edit(
            text=cat_msg,
            reply_markup = keyboard
        )
    elif msg.data == "reports":
        await msg.message.edit(
            text="Welcome to the reports section",
            reply_markup = client_report_button
        )
    
    elif msg.data == "account":
        await msg.message.edit(
            text="Please press the button to generae your wanted report",
            reply_markup = accoun_report_button
        )
    elif msg.data == "rback":
        await msg.message.edit(
            text="Welcome to the reports section",
            reply_markup = client_report_button
        )

    elif msg.data == "cback":
        
        await msg.edit_message_text(
            text=client_msg.format(mention),
            reply_markup = client_button
        )
    
    elif msg.data == "Cservice": 
        
        await msg.edit_message_text(
            text="welcome to service section",
            reply_markup = client_serv_button
        )

    elif msg.data == "accoun":
          
        await msg.edit_message_text(
            text=Accoun_msg,
            reply_markup = InlineKeyboardMarkup(
                [
                [InlineKeyboardButton("Back", callback_data="aback")]
                ]
            )
        )

    elif msg.data == "csback":
        await msg.edit_message_text(
            text=client_msg.format(mention),
            reply_markup = client_serv_button
        )
    
    elif msg.data == "aback":
        
        await msg.edit_message_text(
            text = Member_msg.format(mention),
            reply_markup = Mem_Button
        )


        
    elif msg.data == "fback" or "tback" or "Bback" or "eback":
        await msg.edit_message_text(
            text=com_text,
            reply_markup = serv_button
        )
 


    elif msg.data == "sback" or "clback":
        await msg.delete()
            
"""