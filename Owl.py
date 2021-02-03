import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("키위는 잘생겼습니다!")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await message.channel.send('pong')
    if message.content.startswith('시리야 도와줘'):
        await message.channel.send('Siri가 도와드리겠습니다. 미리 알림을 설정하거나, 날씨를 알아보거나, FaceTime 전화를 거는 등 다양한 작업을 수행해보세요. Apple.com/siri 사이트에서 Siri에 대해 알아보기')
    if message.content.startswith('시리야 자폭해'):
        await message.channel.send('너나해 ^^')
    if message.content.startswith('시리야 ㅋㅋㄹ'):
         await message.channel.send('ㅋㅋㄹㅃㅃ')
    if message.content.startswith('시리야 배고파'):
         await message.channel.send('배민 뒤져 보세요')
    if message.content.startswith('시리야 응애'):
         await message.channel.send('응...응...응애...ㅠ')
    if message.content.startswith('시리야 옹강만'):
        await message.channel.send('아 씨발새끼 꺼지세요    출처-Ganji_YT 님')
    if message.content.startswith('시리야 졸라팝'):
        await message.channel.send('너 밴')
    if message.content.startswith('시리야 빅스비'):
        await message.channel.send('ㅈ까')
    if message.content.startswith('시리야 구글'):
        await message.channel.send('검색결과가 있습니다. 검색 결과 : ㅗ')
    if message.content.startswith('시리야 오케이구글'):
        await message.channel.send('검색결과가 있습니다. 검색결과 : 키위 잘생김')
    if message.content.startswith('시리야 아파'):
        await message.channel.send('긴급신고 119')
    if message.content.startswith('시리야 뭐해'):
        await message.channel.send('너 엿맥일 준비중...')
    if message.content.startswith('시리야 비트박스'):
        await message.channel.send('북치기 박치기 ||대가리 후려치기||')
    if message.content.startswith('시리야 어디살아'):
        await message.channel.send('서울광역시 해운대구 개성공단, 올꺼면 와바')
    if message.content.startswith('시리야 ㅎㅇ'):
        await message.channel.send('ㅃㅇ')
    if message.content.startswith('시리야 요파'):
        await message.channel.send('프본의 근본')
    if message.content.startswith('시리야 카톡'):
        await message.channel.send('친구도 없으면서 뭐할라고')
    if message.content.startswith('시리야 sns'):
        await message.channel.send('팔로잉 밖에 없으면서..')
    if message.content.startswith('시리야 SNS'):
        await message.channel.send('팔로잉 밖에 없으면서..')
    if message.content.startswith('시리야 사랑해'):
        await message.channel.send('메시지가 전송되지 않았어요. 수신자와 공통된 서버가 없거나, 수신자가 친구의 개인 메시지를 받도록 설정했기 때문일 수 있어요. 메시지가 전송되지 않을 수 있는 이유는 다음 목록에서 확인해주세요. https://support.discord.com/hc/ko/articles/360060145013')
    if message.content.startswith('시리야 좋아해'):
        await message.channel.send('메시지가 전송되지 않았어요. 수신자와 공통된 서버가 없거나, 수신자가 친구의 개인 메시지를 받도록 설정했기 때문일 수 있어요. 메시지가 전송되지 않을 수 있는 이유는 다음 목록에서 확인해주세요. https://support.discord.com/hc/ko/articles/360060145013')
    if message.content.startswith('시리야 사귀자'):
        await message.channel.send('메시지가 전송되지 않았어요. 수신자와 공통된 서버가 없거나, 수신자가 친구의 개인 메시지를 받도록 설정했기 때문일 수 있어요. 메시지가 전송되지 않을 수 있는 이유는 다음 목록에서 확인해주세요. https://support.discord.com/hc/ko/articles/360060145013')
    if message.content.startswith('시리야 차님'):
        await message.channel.send('http://bit.ly/차님유튜브   구독과 좋아요!')
    if message.content.startswith('시리야 six'):
        await message.channel.send('식스님 존경합니다')
    if message.content.startswith('시리야 식스'):
        await message.channel.send('멋있고 키도 크시고 잘생기신 식스님')
    if message.content.startswith('시리야 아울'):
        await message.channel.send('목소리가 섹시한 아울')
    if message.content.startswith('시리야 봇추가'):
        await message.channel.send('http://bit.ly/시리봇')
    if message.content.startswith('시리야 추가'):
        await message.channel.send('http://bit.ly/시리봇')
    if message.content.startswith('시리봇 추가'):
        await message.channel.send('http://bit.ly/시리봇')
    if message.content.startswith('섹스'):
        await message.channel.send('제작자 생각좀하자... 이걸 쓰고 있는게 웃기지 않음?ㄹㅇㅋㅋ')
    if message.content.startswith('시리야 섹스'):
        await message.channel.send('미친..')
        await message.channel.send('근데 이 명령어를 쓰는 내가 웃기다ㅋㅋ')
        await message.channel.send('현타옴')
    if message.content.startswith('하이 빅스비'):
        await message.channel.send('착각하셨나본데요, 전 시리입니다!')
    if message.content.startswith('빅스비'):
        await message.channel.send('2017년 3월29일 공개된 삼성전자의 갤럭시S8에 탑재된 인공지능(AI) 가상 비서이다...')
        await message.channel.send('내가 이거 왜 말하고 있음 시린데....')
    if message.content.startswith('시리야 키위'):
        await message.channel.send('저의 제작자는 키위이고, 매우잘생겼습니다!')
    if message.content.startswith('시리야 마코'):
        await message.channel.send(':thinking:')
        await message.channel.send('잘생겼다는데 못믿겠음')
        await message.channel.send('얼공하면 믿어드림ㄹㅇㅋㅋ')
    if message.content.startswith('시리야 날씨'):
        await message.channel.send('http://bit.ly/오늘날씨S')
    if message.content.startswith('시리야 오늘날씨'):
        await message.channel.send('http://bit.ly/오늘날씨S')
    if message.content.startswith('시리야 전번'):
        await message.channel.send('010-661-661')
    if message.content.startswith('시리야 전화번호'):
        await message.channel.send('010-661-661')
    if message.content.startswith('시리야 구피'):
        await message.channel.send('응애가 마려워')
    if message.content.startswith('시리야 고구마'):
        await message.channel.send('호박고구마!!')
    if message.content.startswith('ㄱㄷ'):
        await message.channel.send('난 착해서 기다려줌!')
    if message.content.startswith('헤응'):
        await message.channel.send('...?')
    if message.content.startswith('헤으응'):
        await message.channel.send('ㅔ?')
    if message.content.startswith('시리야 할래'):
        await message.channel.send('네...!')
    if message.content.startswith('시리야 할래?'):
        await message.channel.send('네...!')
    if message.content.startswith('시리야 그거할래'):
        await message.channel.send('네...! 대전 오세요!')
    if message.content.startswith('ㅤ'):
        await message.channel.send('시리봇 이용해주시는건 감사합니다,하지만 이 서버를 19금으로 만드는건 자제 부탁드립니다. 명령어에 있지도 않는 음란한 글은 경고 대상이 될 수 있습니다. 감사합니다. 좋은 하루 보내세요')
    if message.content.startswith('호스팅 종료'):
        await message.channel.send('시리봇 호스팅 종료')
    if message.content.startswith('호스팅 시작'):
        await message.channel.send('시리봇 호스팅 시작')
    if message.content.startswith('아ㅓ랑리ㅏ니ㅟㅏㅜ'):
        await message.channel.send('시리봇 호스팅 시작')
    if message.content.startswith('시리야 시니아'):
        await message.channel.send('내위위시니아')
    if message.content.startswith('시리야 스콧'):
        await message.channel.send('http://bit.ly/스콧   여기서 구독 안누르면 스콧!')
    if message.content.startswith('시리야 빙고'):
        await message.channel.send('=여자')
    if message.content.startswith('시리야 지망'):
        await message.channel.send('망지망지권법')
    if message.content.startswith('시리야 아울'):
        await message.channel.send('목소리가 섹시해...!')
    if message.content.startswith('시리야 잘자'):
        await message.channel.send('잘 자지 말고 새벽에 깨서 피곤하길 바래')
    if message.content.startswith('하이빅스비'):
        await message.channel.send('ㅈ까')
    if message.content.startswith('오케이 구글'):
        await message.channel.send('시리갓')
    if message.content.startswith('시리야 포'):
        await message.channel.send('owo')
    if message.content.startswith('시리야 현거'):
        await message.channel.send('현거는 즉시 밴 이란다^^')
    if message.content.startswith('시리야 초월'):
        await message.channel.send("six 님 따까리")
    if message.content.startswith('시리야 플마'):
        await message.channel.send('http://bit.ly/플마  구독과 좋아요!')
    if message.content.startswith('시리야 희차니'):
        await message.channel.send('누가 나한테 하페 버리면 그랜절')
    if message.content.startswith('시리야 프사'):
        await message.channel.send('https://cdn.discordapp.com/attachments/777742531064365076/806015437284442112/68619211bad02e16.PNG   쓰고 싶으면 쓰세요 - 구드워즈님')
    if message.content.startswith('시리야 롤떠'):
        await message.channel.send('http://bit.ly/롤떠   구독과 좋아요!')
    if message.content.startswith('시리야 당근'):
        await message.channel.send(':carrot:')
        await message.channel.send('살려줘...')
    if message.content.startswith('시리야 김두한'):
        await message.channel.send('김두한은 1972년 11월 21일 오렌지병으로 인해 쓰러졌다...')
        await message.channel.send('http://bit.ly/오렌지병')
    if message.content.startswith('ㅇㅅㅇ'):
        await message.channel.send(f'{message.author.mention},너밴^^')
    if message.content.startswith('시리야 푸세'):
        await message.channel.send(':heart: ..!!')
    if message.content.startswith('시리야 푸른세솔'):
        await message.channel.send('http://bit.ly/sesol  구독과 좋아요!')
    if message.content.startswith('시리야 안녕'):
        await message.channel.send(random.choice(['안 안녕하세요','왜요,,','안녕히가세요','네',f'{message.author.name}, 안녕하세요','ㅃㅇ','ㅎㅇ']))















































client.run('ODA1NjE3MjM5NTI4MzA4NzM3.YBdfhQ.dvgr5tfHUJCRUVMjqycWhTZmMmE')