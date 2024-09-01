import random

tarot_deck = [
    # 大阿卡納 (Major Arcana)
    "愚者",
    "魔法師",
    "女祭司",
    "皇后",
    "皇帝",
    "教皇",
    "戀人",
    "戰車",
    "力量",
    "隱者",
    "命運之輪",
    "正義",
    "倒吊者",
    "死神",
    "節制",
    "惡魔",
    "塔",
    "星星",
    "月亮",
    "太陽",
    "審判",
    "世界",
    # 小阿卡納 (Minor Arcana)
    # 帶有花色的數字牌
    "聖杯1",
    "聖杯2",
    "聖杯3",
    "聖杯4",
    "聖杯5",
    "聖杯6",
    "聖杯7",
    "聖杯8",
    "聖杯9",
    "聖杯10",
    "權杖1",
    "權杖2",
    "權杖3",
    "權杖4",
    "權杖5",
    "權杖6",
    "權杖7",
    "權杖8",
    "權杖9",
    "權杖10",
    "錢幣1",
    "錢幣2",
    "錢幣3",
    "錢幣4",
    "錢幣5",
    "錢幣6",
    "錢幣7",
    "錢幣8",
    "錢幣9",
    "錢幣10",
    "劍1",
    "劍2",
    "劍3",
    "劍4",
    "劍5",
    "劍6",
    "劍7",
    "劍8",
    "劍9",
    "劍10",
    # 帶有花色的面值牌
    "聖杯騎士",
    "聖杯女王",
    "聖杯國王",
    "聖杯侍者",
    "權杖騎士",
    "權杖女王",
    "權杖國王",
    "權杖侍者",
    "錢幣騎士",
    "錢幣女王",
    "錢幣國王",
    "錢幣侍者",
    "劍騎士",
    "劍女王",
    "劍國王",
    "劍侍者"
]

#=============================列出說明===============================#


def guide():

  text = [
      "說明",
      "輸入1或抽一張牌：抽一張牌",
      "輸入2或時間之流：抽時間流",
      "輸入3或抽聖三角：抽聖三角",
      "輸入4或抽六芒星：抽六芒星",
      "輸入5或抽無牌陣：抽無牌陣",
      "輸入6或抽關係牌：抽關係牌",
  ]

  return '\n'.join(text)


#=============================抽一張牌===============================#


def draw_one_cards(question):

  cards = random.sample(tarot_deck, 1)

  text = [
      question,
      "一抽：" + cards[0],
  ]

  return '\n'.join(text)


#=============================抽時間之流===============================#


def draw_timeflow_cards(question):

  cards = random.sample(tarot_deck, 3)

  text = [
      question,
      "時間之流：",
      "過去：" + cards[0],
      "現在：" + cards[1],
      "未來：" + cards[2],
  ]

  return '\n'.join(text)


#=============================抽聖三角===============================#


def draw_triangle_cards(question):

  cards = random.sample(tarot_deck, 3)

  text = [
      question,
      "聖三角：",
      "現況：" + cards[0],
      "問題：" + cards[1],
      "建議：" + cards[2],
  ]

  return '\n'.join(text)


#=============================抽六芒星===============================#


def draw_sixstar_cards(question):

  cards = random.sample(tarot_deck, 7)

  text = [
      question,
      "六芒星：",
      "過去：" + cards[0],
      "現在：" + cards[1],
      "未來：" + cards[2],
      "障礙：" + cards[3],
      "建議：" + cards[4],
      "環境：" + cards[5],
      "結果：" + cards[6],
  ]

  return '\n'.join(text)


#=============================抽無牌陣===============================#


def draw_three_cards(question):

  cards = random.sample(tarot_deck, 3)

  text = [
      question,
      "三張無牌陣：",
      "第一張牌：" + cards[0],
      "第二張牌：" + cards[1],
      "第三張牌：" + cards[2],
  ]

  return '\n'.join(text)


#=============================抽關係牌陣===============================#


def draw_relation_cards(question):

  cards = random.sample(tarot_deck, 4)

  text = [
      question,
      "關係牌陣：",
      "現在關係現狀：" + cards[0],
      "當事人在關係的現況/想法：" + cards[1],
      "對方在關係的現況/想法：" + cards[2],
      "關係未來發展：" + cards[3],
  ]

  return '\n'.join(text)