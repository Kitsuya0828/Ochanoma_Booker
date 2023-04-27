def view_home(user):
    view = {
            "type": "home",
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "お茶の間予約システム :coffee:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": (f"<@{user}>さん、ここでお茶の間の予約をしてみよう :tada:\n"
                                 "予約状況は<https://calendar.google.com/calendar/u/0?cid=Y19uNzNwbGVzZWtxYXRzanU2aDFjcTFibjJhc0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t|*ここ*>から見てね :eyes:\n"
                                 "使い方は<https://scrapbox.io/iiclab/OchanomaBooker%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9|*Scrapbox*>を参考にしてね :green_book:\n")
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "input",
                    "element": {
                        "type": "datepicker",
                        #"initial_date": "2022-08-01",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select a date"
                        },
                        "action_id": "datepick"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": ":calendar: 日付",
                        "emoji": True
                    },
                    "block_id": "dateblock"
                },
                {
                    "type": "input",
                    "element": {
                            "type": "timepicker",
                            #"initial_time": "00:00",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select start time"
                            },
                            "action_id": "timepick"
                        },
                    "label": {
                        "type": "plain_text",
                        "text": ":alarm_clock: 開始時間",
                        "emoji": True
                    },
                    "block_id": 'start_time_block'
                },
                {
                    "type": "input",
                    "element": {
                            "type": "timepicker",
                            #"initial_time": "00:00",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select end time"
                            },
                            "action_id": "timepick"
                        },
                    "label": {
                        "type": "plain_text",
                        "text": ":alarm_clock: 終了時間",
                        "emoji": True
                    },
                    "block_id": 'end_time_block'
                },
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": "[注] 分刻みの場合は直接入力する事ができるよ！"
                    }
                },
                {
                    "type": "input",
                    "element": {
                            "type": "plain_text_input",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Write description"
                            },
                            "action_id": "description"
                        },
                    "label": {
                        "type": "plain_text",
                        "text": ":mag: 詳細 (任意入力)",
                        "emoji": True
                    },
                    "block_id": 'textblock'
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "style": "primary",
                            "text": {
                                "type": "plain_text",
                                "text": "追加"
                            },
                            "value": "home_add",
                            "action_id": "add_home"
                        }
                    ]
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": " ",
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": " ",
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":busts_in_silhouette: *みんなの予約*",
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "確認"
                        },
                        "value": "home_check",
                        "action_id": "check_home"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":bust_in_silhouette: *自分の予約*",
                    },
                    "accessory": {
                        "type": "button",
                        "style": "danger",
                        "text": {
                            "type": "plain_text",
                            "text": "確認・削除"
                        },
                        "value": "home_delete",
                        "action_id": "delete_home"
                    }
                },
            ]
        }

    return view

def view_schedule(text):
    view={
            "type": "modal",
            "callback_id": "view_before",
            "title": {"type": "plain_text", "text":"Schedule"},
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ("checking schedule")}
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": text
                    }
                }
            ]
        }

    return view


def view_check(calendar_info):
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ("The list of schedules at the tea room is shown below. :memo:\n"
                            "This list is based on the data collected by this bot, and may be different from the actual state:exclamation:")}
        },
    ]

    for ci in calendar_info:
        blocks.append({"type": "divider"})
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ci
            }
        })

    view={
            "type": "modal",
            "callback_id": "view_member",
            "title": {"type": "plain_text", "text":"みんなの予約状況"},
            # "blocks": [
            #     {
            #         "type": "section",
            #         "text": {
            #             "type": "mrkdwn",
            #             "text": ("The list of schedules at the tea room is shown below. :memo:\n"
            #                      "This list is based on the data collected by this bot, and may be different from the actual state:exclamation:")}
            #     },
            #     {
            #         "type": "divider"
            #     },
            #     {
            #         "type": "section",
            #             "text": {
            #                 "type": "mrkdwn",
            #                 "text": calendar_info
            #             }
            #     }
            # ]
            "blocks": blocks,
        }

    return view

def view_cancel(user_id, user_schedule_list):
    if len(user_schedule_list) == 0:
        return {
            "type": "modal",
            "title": {"type": "plain_text", "text":"あなたの予約"},
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"<@{user_id}>さんには、削除可能な予約がありませんでした :cry:"
                    }
                },
            ]
        }
    
    view = {
            "type": "modal",
            "callback_id": "view_cancel_delete",
            "title": {"type": "plain_text", "text":"あなたの予約"},
            "submit": {"type": "plain_text", "text": "削除"},
            "blocks": [
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": (f"<@{user_id}>さんの予約のみが表示されます。\n削除する場合は、予約を1つ選択して *削除* ボタンを押してください。")
                    }
                },
                {
                    "type": "input",
                    "block_id": "selected_schedule",
                    "element": {
                        "type": "static_select",
                        "options": user_schedule_list,
                        "action_id": "static_select-action",
                    },
                    "label": {
                        "type": "plain_text",
                        "text": " ",
                    }
                }
            ]
        }
    return view

def view_duplicate(user):
    view = {
        "type": "modal",
        "close": {
            "type": "plain_text",
            "text": "Close",
            "emoji": True
        },
        "title": {
            "type": "plain_text",
            "text": "予定が重複しています。",
            "emoji": True
        },
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f":wave: Hey <@{user}>!\n\nSorry, your selected time is already reserved.\nPlease select another time."
                }
            }
        ]
    }
    return view

def view_delete_fail(user):
    view = {
        "type": "modal",
        "close": {
            "type": "plain_text",
            "text": "Close",
            "emoji": True
        },
        "title": {
            "type": "plain_text",
            "text": "予定が削除できませんでした。",
            "emoji": True
        },
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f":wave: Hey <@{user}>!\n\nSorry, reservation could not be deleted for some reason..."
                }
            }
        ]
    }
    return view