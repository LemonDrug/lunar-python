# -*- coding: utf-8 -*-
from .util import LunarUtil


class EightChar:
    """
    八字
    """

    MONTH_ZHI = ("", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥", "子", "丑")

    CHANG_SHENG = ("长生", "沐浴", "冠带", "临官", "帝旺", "衰", "病", "死", "墓", "绝", "胎", "养")

    __CHANG_SHENG_OFFSET = {
        "甲": 1,
        "丙": 10,
        "戊": 10,
        "庚": 7,
        "壬": 4,
        "乙": 6,
        "丁": 9,
        "己": 9,
        "辛": 0,
        "癸": 3
    }

    def __init__(self, lunar):
        self.__sect = 2
        self.__lunar = lunar

    @staticmethod
    def fromLunar(lunar):
        return EightChar(lunar)

    def toString(self):
        return self.getYear() + " " + self.getMonth() + " " + self.getDay() + " " + self.getTime()

    def __str__(self):
        return self.toString()

    def getSect(self):
        return self.__sect

    def setSect(self, sect):
        self.__sect = sect

    def getYear(self):
        """
        获取年柱
        :return: 年柱
        """
        return self.__lunar.getYearInGanZhiExact()

    def getYearGan(self):
        """
        获取年干
        :return: 天干
        """
        return self.__lunar.getYearGanExact()

    def getYearZhi(self):
        """
        获取年支
        :return: 地支
        """
        return self.__lunar.getYearZhiExact()

    def getYearHideGan(self):
        """
        获取年柱地支藏干，由于藏干分主气、余气、杂气，所以返回结果可能为1到3个元素
        :return: 天干
        """
        return LunarUtil.ZHI_HIDE_GAN.get(self.getYearZhi())

    def getYearWuXing(self):
        """
        获取年柱五行
        :return: 五行
        """
        return LunarUtil.WU_XING_GAN.get(self.getYearGan()) + LunarUtil.WU_XING_ZHI.get(self.getYearZhi())

    def getYearNaYin(self):
        """
        获取年柱纳音
        :return: 纳音
        """
        return LunarUtil.NAYIN.get(self.getYear())

    def getYearShiShenGan(self):
        """
        获取年柱天干十神
        :return: 十神
        """
        return LunarUtil.SHI_SHEN_GAN.get(self.getDayGan() + self.getYearGan())

    def __getShiShenZhi(self, zhi):
        hideGan = LunarUtil.ZHI_HIDE_GAN.get(zhi)
        l = []
        for gan in hideGan:
            l.append(LunarUtil.SHI_SHEN_ZHI.get(self.getDayGan() + zhi + gan))
        return l

    def getYearShiShenZhi(self):
        """
        获取年柱地支十神，由于藏干分主气、余气、杂气，所以返回结果可能为1到3个元素
        :return: 十神
        """
        return self.__getShiShenZhi(self.getYearZhi())

    def getDayGanIndex(self):
        return self.__lunar.getDayGanIndexExact2() if 2 == self.__sect else self.__lunar.getDayGanIndexExact()

    def getDayZhiIndex(self):
        return self.__lunar.getDayZhiIndexExact2() if 2 == self.__sect else self.__lunar.getDayZhiIndexExact()

    def __getDiShi(self, zhiIndex):
        offset = self.__CHANG_SHENG_OFFSET.get(self.getDayGan())
        index = offset + (zhiIndex if self.getDayGanIndex() % 2 == 0 else zhiIndex)
        if index >= 12:
            index -= 12
        if index < 0:
            index += 12
        return EightChar.CHANG_SHENG[index]

    def getYearDiShi(self):
        """
        获取年柱地势（长生十二神）
        :return: 地势
        """
        return self.__getDiShi(self.__lunar.getYearZhiIndexExact())

    def getMonth(self):
        """
        获取月柱
        :return: 月柱
        """
        return self.__lunar.getMonthInGanZhiExact()

    def getMonthGan(self):
        """
        获取月干
        :return: 天干
        """
        return self.__lunar.getMonthGanExact()

    def getMonthZhi(self):
        """
        获取月支
        :return: 地支
        """
        return self.__lunar.getMonthZhiExact()

    def getMonthHideGan(self):
        """
        获取月柱地支藏干，由于藏干分主气、余气、杂气，所以返回结果可能为1到3个元素
        :return: 天干
        """
        return LunarUtil.ZHI_HIDE_GAN.get(self.getMonthZhi())

    def getMonthWuXing(self):
        """
        获取月柱五行
        :return: 五行
        """
        return LunarUtil.WU_XING_GAN.get(self.getMonthGan()) + LunarUtil.WU_XING_ZHI.get(self.getMonthZhi())

    def getMonthNaYin(self):
        """
        获取月柱纳音
        :return: 纳音
        """
        return LunarUtil.NAYIN.get(self.getMonth())

    def getMonthShiShenGan(self):
        """
        获取月柱天干十神
        :return: 十神
        """
        return LunarUtil.SHI_SHEN_GAN.get(self.getDayGan() + self.getMonthGan())

    def getMonthShiShenZhi(self):
        """
        获取月柱地支十神，由于藏干分主气、余气、杂气，所以返回结果可能为1到3个元素
        :return: 十神
        """
        return self.__getShiShenZhi(self.getMonthZhi())

    def getMonthDiShi(self):
        """
        获取月柱地势（长生十二神）
        :return: 地势
        """
        return self.__getDiShi(self.__lunar.getMonthZhiIndexExact())

    def getDay(self):
        """
        获取日柱
        :return: 日柱
        """
        return self.__lunar.getDayInGanZhiExact2() if 2 == self.__sect else self.__lunar.getDayInGanZhiExact()

    def getDayGan(self):
        """
        获取日干
        :return: 天干
        """
        return self.__lunar.getDayGanExact2() if 2 == self.__sect else self.__lunar.getDayGanExact()

    def getDayZhi(self):
        """
        获取日支
        :return: 地支
        """
        return self.__lunar.getDayZhiExact2() if 2 == self.__sect else self.__lunar.getDayZhiExact()

    def getDayHideGan(self):
        """
        获取日柱地支藏干，由于藏干分主气、余气、杂气，所以返回结果可能为1到3个元素
        :return: 天干
        """
        return LunarUtil.ZHI_HIDE_GAN.get(self.getDayZhi())

    def getDayWuXing(self):
        """
        获取日柱五行
        :return: 五行
        """
        return LunarUtil.WU_XING_GAN.get(self.getDayGan()) + LunarUtil.WU_XING_ZHI.get(self.getDayZhi())

    def getDayNaYin(self):
        """
        获取日柱纳音
        :return: 纳音
        """
        return LunarUtil.NAYIN.get(self.getDay())

    def getDayShiShenGan(self):
        """
        获取日柱天干十神，也称日元、日干
        :return: 十神
        """
        return "日主"

    def getDayShiShenZhi(self):
        """
        获取日柱地支十神，由于藏干分主气、余气、杂气，所以返回结果可能为1到3个元素
        :return: 十神
        """
        return self.__getShiShenZhi(self.getDayZhi())

    def getDayDiShi(self):
        """
        获取日柱地势（长生十二神）
        :return: 地势
        """
        return self.__getDiShi(self.getDayZhiIndex())

    def getTime(self):
        """
        获取时柱
        :return: 时柱
        """
        return self.__lunar.getTimeInGanZhi()

    def getTimeGan(self):
        """
        获取时干
        :return: 天干
        """
        return self.__lunar.getTimeGan()

    def getTimeZhi(self):
        """
        获取时支
        :return: 地支
        """
        return self.__lunar.getTimeZhi()

    def getTimeHideGan(self):
        """
        获取时柱地支藏干，由于藏干分主气、余气、杂气，所以返回结果可能为1到3个元素
        :return: 天干
        """
        return LunarUtil.ZHI_HIDE_GAN.get(self.getTimeZhi())

    def getTimeWuXing(self):
        """
        获取时柱五行
        :return: 五行
        """
        return LunarUtil.WU_XING_GAN.get(self.getTimeGan()) + LunarUtil.WU_XING_ZHI.get(self.getTimeZhi())

    def getTimeNaYin(self):
        """
        获取时柱纳音
        :return: 纳音
        """
        return LunarUtil.NAYIN.get(self.getTime())

    def getTimeShiShenGan(self):
        """
        获取时柱天干十神
        :return: 十神
        """
        return LunarUtil.SHI_SHEN_GAN.get(self.getDayGan() + self.getTimeGan())

    def getTimeShiShenZhi(self):
        """
        获取时柱地支十神，由于藏干分主气、余气、杂气，所以返回结果可能为1到3个元素
        :return: 十神
        """
        return self.__getShiShenZhi(self.getTimeZhi())

    def getTimeDiShi(self):
        """
        获取时柱地势（长生十二神）
        :return: 地势
        """
        return self.__getDiShi(self.__lunar.getTimeZhiIndex())

    def getTaiYuan(self):
        """
        获取胎元
        :return: 胎元
        """
        ganIndex = self.__lunar.getMonthGanIndexExact() + 1
        if ganIndex >= 10:
            ganIndex -= 10
        zhiIndex = self.__lunar.getMonthZhiIndexExact() + 3
        if zhiIndex >= 12:
            zhiIndex -= 12
        return LunarUtil.GAN[ganIndex + 1] + LunarUtil.ZHI[zhiIndex + 1]

    def getTaiYuanNaYin(self):
        """
        获取胎元纳音
        :return: 纳音
        """
        return LunarUtil.NAYIN.get(self.getTaiYuan())

    def getMingGong(self):
        """
        获取命宫
        :return: 命宫
        """
        monthZhiIndex = 0
        timeZhiIndex = 0
        for i in range(0, len(EightChar.MONTH_ZHI)):
            zhi = EightChar.MONTH_ZHI[i]
            if self.__lunar.getMonthZhiExact() == zhi:
                monthZhiIndex = i

            if self.__lunar.getTimeZhi() == zhi:
                timeZhiIndex = i

        zhiIndex = 26 - (monthZhiIndex + timeZhiIndex)
        if zhiIndex > 12:
            zhiIndex -= 12
        jiaZiIndex = LunarUtil.getJiaZiIndex(self.getMonth()) - (monthZhiIndex - zhiIndex)
        if jiaZiIndex >= 60:
            jiaZiIndex -= 60
        if jiaZiIndex < 0:
            jiaZiIndex += 60
        return LunarUtil.JIA_ZI[jiaZiIndex]

    def getMingGongNaYin(self):
        """
        获取命宫纳音
        :return: 纳音
        """
        return LunarUtil.NAYIN.get(self.getMingGong())

    def getShenGong(self):
        """
        获取身宫
        :return: 身宫
        """
        monthZhiIndex = 0
        timeZhiIndex = 0
        for i in range(0, len(EightChar.MONTH_ZHI)):
            zhi = EightChar.MONTH_ZHI[i]
            if self.__lunar.getMonthZhiExact() == zhi:
                monthZhiIndex = i

            if self.__lunar.getTimeZhi() == zhi:
                timeZhiIndex = i

        zhiIndex = (2 + (monthZhiIndex + timeZhiIndex)) % 12
        jiaZiIndex = LunarUtil.getJiaZiIndex(self.getMonth()) - (monthZhiIndex - zhiIndex)
        if jiaZiIndex >= 60:
            jiaZiIndex -= 60
        if jiaZiIndex < 0:
            jiaZiIndex += 60
        return LunarUtil.JIA_ZI[jiaZiIndex]

    def getShenGongNaYin(self):
        """
        获取身宫纳音
        :return: 纳音
        """
        return LunarUtil.NAYIN.get(self.getShenGong())

    def getLunar(self):
        return self.__lunar

    def getYun(self, gender):
        """
        获取运
        :param gender: 性别：1男，0女
        :return: 运
        """
        from .eightchar import Yun
        return Yun(self, gender)

    def getYearXun(self):
        """
        获取年柱所在旬
        :return: 旬
        """
        return self.__lunar.getYearXunExact()

    def getYearXunKong(self):
        """
        获取年柱旬空(空亡)
        :return: 旬空(空亡)
        """
        return self.__lunar.getYearXunKongExact()

    def getMonthXun(self):
        """
        获取月柱所在旬
        :return: 旬
        """
        return self.__lunar.getMonthXunExact()

    def getMonthXunKong(self):
        """
        获取月柱旬空(空亡)
        :return: 旬空(空亡)
        """
        return self.__lunar.getMonthXunKongExact()

    def getDayXun(self):
        """
        获取日柱所在旬
        :return: 旬
        """
        return self.__lunar.getDayXunExact2() if 2 == self.__sect else self.__lunar.getDayXunExact()

    def getDayXunKong(self):
        """
        获取日柱旬空(空亡)
        :return: 旬空(空亡)
        """
        return self.__lunar.getDayXunKongExact2() if 2 == self.__sect else self.__lunar.getDayXunKongExact()

    def getTimeXun(self):
        """
        获取时柱所在旬
        :return: 旬
        """
        return self.__lunar.getTimeXun()

    def getTimeXunKong(self):
        """
        获取时柱旬空(空亡)
        :return: 旬空(空亡)
        """
        return self.__lunar.getTimeXunKong()