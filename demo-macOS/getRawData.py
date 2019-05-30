import IAgoraRtcEngine

appId = b"466c2ed3224c4e42996f7e08d2bb7193"

Engine = IAgoraRtcEngine.pycreateAgoraRtcEngine()
ctx = IAgoraRtcEngine.pyRtcEngineContext()
ctx.eventHandler = IAgoraRtcEngine.pyEventHandler()
ctx.appId = appId
Engine.initialize(ctx)
Engine.joinChannel(appId, b"123", b"", 0)

Engine.enableVideo()
EngineParam = IAgoraRtcEngine.pyRtcEngineParameters()
EngineParam.construct_3(Engine)
EngineParam.enableLocalVideo(True)
EngineParam.muteLocalVideoStream(False)

MediaEngine = IAgoraRtcEngine.pyGetMediaEngine(Engine)
MediaEngine.registerVideoFrameObserver(IAgoraRtcEngine.pyVideoFrameObserver())

_ = input("press any key to disconnect")
Engine.release(False)
