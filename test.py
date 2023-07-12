from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TemplateSendMessage,URIAction,ButtonsTemplate,PostbackEvent,MessageTemplateAction,PostbackTemplateAction# 載入 TextSendMessage 模組
from linebot.models import MessageEvent, TextMessage,TextSendMessage, ImageSendMessage, StickerSendMessage,LocationSendMessage, QuickReply, QuickReplyButton, MessageAction,FlexSendMessage
reviews=''
#555555555555555
TemplateSendMessage(
    alt_text='Buttons IMDb',
    template=ButtonsTemplate(
        title='進階搜尋',
        text='請選擇要尋找的',
        actions=[
            PostbackTemplateAction(
                label=reviews[1][0],
                display_text=reviews[1][0],
                data=f'M{reviews[2][0]}'
            ),
            PostbackTemplateAction(
                label=reviews[1][1],
                display_text=reviews[1][1],
                data=f'M{reviews[2][1]}'
            ),
            PostbackTemplateAction(
                label=reviews[1][2],
                display_text=reviews[1][2],
                data=f'M{reviews[2][2]}',
            ),
            PostbackTemplateAction(
                label=reviews[1][3],
                display_text=reviews[1][3],
                data=f'M{reviews[2][3]}',
            ),PostbackTemplateAction(
                label=reviews[1][4],
                display_text=reviews[1][4],
                data=f'M{reviews[2][4]}'
            )]))
#44444444444
TemplateSendMessage(
    alt_text='Buttons IMDb',
    template=ButtonsTemplate(
        title='進階搜尋',
        text='請選擇要尋找的',
        actions=[
            PostbackTemplateAction(
                label=reviews[1][0],
                display_text=reviews[1][0],
                data=f'M{reviews[2][0]}'
            ),
            PostbackTemplateAction(
                label=reviews[1][1],
                display_text=reviews[1][1],
                data=f'M{reviews[2][1]}'
            ),
            PostbackTemplateAction(
                label=reviews[1][2],
                display_text=reviews[1][2],
                data=f'M{reviews[2][2]}',
            ),
            PostbackTemplateAction(
                label=reviews[1][3],
                display_text=reviews[1][3],
                data=f'M{reviews[2][3]}',
            ),]))
#333333333333333333333
TemplateSendMessage(
    alt_text='Buttons IMDb',
    template=ButtonsTemplate(
        title='進階搜尋',
        text='請選擇要尋找的',
        actions=[
            PostbackTemplateAction(
                label=reviews[1][0],
                display_text=reviews[1][0],
                data=f'M{reviews[2][0]}'
            ),
            PostbackTemplateAction(
                label=reviews[1][1],
                display_text=reviews[1][1],
                data=f'M{reviews[2][1]}'
            ),
            PostbackTemplateAction(
                label=reviews[1][2],
                display_text=reviews[1][2],
                data=f'M{reviews[2][2]}',
            ),
]))
#22222222222222222222
TemplateSendMessage(
    alt_text='Buttons IMDb',
    template=ButtonsTemplate(
        title='進階搜尋',
        text='請選擇要尋找的',
        actions=[
            PostbackTemplateAction(
                label=reviews[1][0],
                display_text=reviews[1][0],
                data=f'M{reviews[2][0]}'
            ),
            PostbackTemplateAction(
                label=reviews[1][1],
                display_text=reviews[1][1],
                data=f'M{reviews[2][1]}'
            ),
]))
#11111111111111111111
TemplateSendMessage(
    alt_text='Buttons IMDb',
    template=ButtonsTemplate(
        title='進階搜尋',
        text='請選擇要尋找的',
        actions=[
            PostbackTemplateAction(
                label=reviews[1][0],
                display_text=reviews[1][0],
                data=f'M{reviews[2][0]}'
            ),
]))


        # if IMDb_result_count>=3:
        #     reply_msg=[TextSendMessage(text=movie_info),
        #                 TemplateSendMessage(
        #                         alt_text='Buttons IMDb',
        #                         template=ButtonsTemplate(
        #                             title='進階搜尋',
        #                             text='請選擇要尋找的',
        #                             actions=[
        #                                 MessageAction(
        #                                     label=f'{IMDb_moviename[0]}',
        #                                     text=f'M{movie_name}&{str(IMDb_link[0])}',
        #                                 ),
        #                                 MessageAction(
        #                                     label=f'{IMDb_moviename[1]}',
        #                                     text=f'M{movie_name}&{str(IMDb_link[1])}',
        #                                 ),
        #                                 MessageAction(
        #                                     label=f'{IMDb_moviename[2]}',
        #                                     text=f'M{movie_name}&{str(IMDb_link[2])}',
        #                                 ),
        #                                 MessageAction(
        #                                     label=f'{IMDb_moviename[3]}',
        #                                     text=f'M{movie_name}&{str(IMDb_link[3])}',
        #                                 )]))]
        if IMDb_result_count>=3:
            reply_msg=[TextSendMessage(text=movie_info),
                        TemplateSendMessage(
                                alt_text='Buttons IMDb',
                                template=ButtonsTemplate(
                                    title='進階搜尋',
                                    text='請選擇要尋找的',
                                    actions=[
                                        MessageAction(
                                            label=f'1',
                                            text=f'M{movie_name}&{IMDb_link[0]}',
                                        ),
                                        MessageAction(
                                            label=f'2',
                                            text=f'M{movie_name}&{IMDb_link[1]}',
                                        ),
                                        MessageAction(
                                            label=f'3',
                                            text=f'M{movie_name}&{IMDb_link[2]}',
                                        ),
                                        ]))]
        elif IMDb_result_count==2:
            reply_msg=[TextSendMessage(text=movie_info),
                        TemplateSendMessage(
                                alt_text='Buttons IMDb',
                                template=ButtonsTemplate(
                                    title='進階搜尋',
                                    text='請選擇要尋找的',
                                    actions=[
                                        MessageAction(
                                            label=f'1',
                                            text=f'M{movie_name}&{IMDb_link[0]}',
                                        ),
                                        MessageAction(
                                            label=f'2',
                                            text=f'M{movie_name}&{IMDb_link[1]}',
                                        ),
                                        ]))]        
        elif IMDb_result_count==1:
            reply_msg=[TextSendMessage(text=movie_info),
                        TemplateSendMessage(
                                alt_text='Buttons IMDb',
                                template=ButtonsTemplate(
                                    title='進階搜尋',
                                    text='請選擇要尋找的',
                                    actions=[
                                        MessageAction(
                                            label=f'1',
                                            text=f'M{movie_name}&{IMDb_link[0]}',
                                        ),
                                        ]))]   