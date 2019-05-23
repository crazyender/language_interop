# -*- coding: utf-8 -*-
import IAgoraRtcEngine
import ctypes
class CallBackData:
    def __init__(self):
        self.localUid = -1
        self.remoteUid = -1
        self.joinChannelSuccess = False

EventHandlerData = CallBackData()

class EventHandler:
    @staticmethod
    def onJoinChannelSuccess(channel, uid, elapsed):
        print ("JoinChannelSuccess: channel=%s, uid=%d, elapsed=%d"%(channel, uid, elapsed))
        EventHandlerData.localUid = uid
        EventHandlerData.joinChannelSuccess = True

    @staticmethod
    def onLeaveChannel(duration, txBytes, rxBytes, txKBitRate,
        rxKBitRate, rxAudioKBitRate, txAudioKBitRate, rxVideoKBitRate,
        txVideoKBitRate, lastmileDelay, userCount, cpuAppUsage,
        cpuTotalUsage):
        EventHandlerData.joinChannelSuccess = False
        EventHandlerData.localUid = -1
        EventHandlerData.remoteUid = -1


    @staticmethod
    def onClientRoleChanged(oldRole, newRole):
        pass

    @staticmethod
    def onConnectionStateChanged(state, reason):
        pass

    @staticmethod
    def onConnectionLost():
        print ("connection lost")

    @staticmethod
    def onRejoinChannelSuccess(channel, uid, elapsed):
        print ("rejoin channel success")

    @staticmethod
    def onUserJoined(uid, elapsed):
        print ("a remote user joined, uid=%d"%uid)
        EventHandlerData.remoteUid = uid

    @staticmethod
    def onUserOffline(uid, reason):
        print ("a remote user offline, uid=%d, reason=%d"%(uid, reason))

    @staticmethod
    def onFirstLocalAudioFrame(elapsed):
        pass

    @staticmethod
    def onMicrophoneEnabled(enabled):
        if enabled:
            print ("microphone enabled")

    @staticmethod
    def onUserEnableVideo(uid, enabled):
        print ("UserEnableVideo, uid=%d"%uid)

    @staticmethod
    def onFirstRemoteAudioFrame(uid, elapsed):
        print ("first remote audio frame, uid=%d" % uid)

    @staticmethod
    def onFirstRemoteVideoDecoded(uid, width, height, elapsed):
        print ("FirstRemoteVideoDecoded: uid=%d, width=%d, height=%d, elapsed=%d" % (uid, width, height, elapsed))

    @staticmethod
    def onNetworkQuality(uid, txQuality, rxQuality):
        pass

    @staticmethod
    def onAudioQuality(uid, quality, delay, lost):
        pass

    @staticmethod
    def onRtcStats(duration, txBytes, rxBytes, txKBitRate,
        rxKBitRate, rxAudioKBitRate, txAudioKBitRate, rxVideoKBitRate,
        txVideoKBitRate, lastmileDelay, userCount, cpuAppUsage,
        cpuTotalUsage):
        pass

    @staticmethod
    def onLocalVideoStats(sentBitrate, sentFrameRate):
        pass

    @staticmethod
    def onUserEnableLocalVideo(uid, enabled):
        pass

    @staticmethod
    def onRemoteVideoStats(uid, delay, width, height, receivedBitrate,
			receivedFrameRate, rxStreamType):
        pass

    @staticmethod
    def onRemoteAudioTransportStats(uid, delay, lost, rxKBitRate):
        pass

    @staticmethod
    def onRemoteVideoTransportStats(uid, delay, lost, rxKBitRate):
        pass

    @staticmethod
    def onApiCallExecuted(err, api, result):
        pass

    @staticmethod
    def onRemoteAudioStats(uid, quality,
			networkTransportDelay, jitterBufferDelay,
			audioLossRate):
        pass

    @staticmethod
    def onCameraReady():
        pass

    @staticmethod
    def onFirstLocalVideoFrame(width, height, elapsed):
        pass

    @staticmethod
    def onRemoteVideoStateChanged(uid, state):
        pass

    @staticmethod
    def onConnectionInterrupted():
        print ("connection lost")

    @staticmethod
    def onFirstRemoteVideoFrame(uid, width, height, elapsed):
        pass

class VideoFrameObserver:
    @staticmethod
    def onCaptureVideoFrame(width, height, yStride,
			uStride, vStride, yBuffer, uBuffer, vBuffer,
			rotation, renderTimeMs, avsync_type):
        array = ctypes.cast(yBuffer, ctypes.POINTER(ctypes.c_byte*yStride))
        print (array)


    @staticmethod
    def onRenderVideoFrame(uid, width, height, yStride,
                            uStride, vStride, yBuffer, uBuffer, vBuffer,
                            rotation, renderTimeMs, avsync_type):
        pass