#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Network import CorpusGraph
from Network import TextGraph
from ResultReference import JiebaChecker
from ResultReference import ThulacChecker

cg = CorpusGraph()
# cg.build_corpus()
# cg.save_as_json('./data/ten.json')
cg.load_from_json()
jieba_checker = JiebaChecker()
thulac_checker = ThulacChecker()

def tokenize(sentence):
    tg = TextGraph()
    tg.build([sentence])
    tg.fill_edge(cg)

    # 暂时只对单句分词
    result = tg.cut()[0]
    jieba_check = jieba_checker.check(sentence, result)
    thulac_check = thulac_checker.check(sentence, result)

    jieba_result = jieba_check["jieba_result"]
    jieba_overlap = jieba_check["overlap"]

    thulac_result = thulac_check["thulac_result"]
    thulac_overlap = thulac_check["overlap"]
    res = {"sentence": sentence, "result": result, "jieba": jieba_result, "jieba_overlap": jieba_overlap,"thulac":thulac_result,"thulac_overlap":thulac_overlap}
    return res

def batching(parag):
    j = 0
    cut = []
    for i in range(0,len(parag)-1):
        if(parag[i] == '。'):
            cut.append(tokenize(parag[j:i]))
            j = i+1
    return cut

if __name__ == '__main__':
    jieba_sum = 0.0
    thulac_sum = 0.0
    cut = batching("广西壮族自治区武宣县人民法院 民事判决书 （2015）武民初字第935号 原告：余生才，农民。 委托代理人：潘杰，广西冠益律师事务所律师。 被告：韦少海，自由职业。 被告：陈世刚，自由职业。 被告：中国人民财产保险股份有限公司柳州市分公司；住所地：柳州市中山中路37号。 代表人：陈雪斌，该公司总经理。 委托代理人：粟光荣，广西华震律师事务所律师。 原告余生才与被告韦少海、陈世刚、中国人民财产保险股份有限公司柳州市分公司（以下简称中财保柳州分公司）机动车交通事故责任纠纷一案，本院于2015年9月6日受理后，依法适用简易程序，于2015年10月14日公开开庭审理了本案。原告余生才及其委托代理人潘杰，被告韦少海、陈世刚，被告中财保柳州分公司委托代理人粟光荣均到庭参加诉讼。本案现已审理终结。 原告余生才诉称，2012年11月20日，原告余生才驾驶桂01-G2242号多功能拖拉机由覃塘往武宣方向行驶，被告韦少海驾驶桂B×××××号小型普通客车由武宣县城往覃塘方向行驶。车辆行驶至G-209线3066km＋670m处时，被告韦少海未按交通信号通行，碰撞了原告驾驶的桂01-G2242号多功能拖拉机，造成原告双胫腓骨骨折，全身多处软组织挫裂伤，桂01-G2242号拖拉机损坏的道路交通事故。武宣县交通警察大队作出武公交认字（2013）第005号《道路交通事故认定书》认定，被告韦少海承担全部责任，原告余生才不承担责任。因这起交通事故给原告造成双腿骨折及全身多处受伤，经鉴定，原告余生才构成两个十级伤残。该起事故给原告的身体和精神造成巨大的痛苦，被告应当给原告予以充分的精神赔偿。2013年3月21日，原告曾就医疗费等费用起诉，2013年6月5日，武宣县人民法院作出（2013年）武民初字第306号民事判决。现经过治疗终结及伤残鉴定，就未请求部分提起诉讼，请求法院：一、判决被告赔偿医药费7345．68元、残疾赔偿金45390元、护理费1020元、交通住宿费1000元、住院伙食补助费1000元、营养费1000元、被扶养人生活费113475元、误工费4000元、鉴定费1400元、精神损害抚慰金10000元、车辆损失9545元、货物损失6360元，合计201535．68元。以上损失由中财保柳州分公司在交强险赔偿限额内先行赔偿，不足部分在商业第三者险赔偿限额内赔偿，再有不足，由韦少海、陈世刚承担连带赔偿责任。二、本案诉讼费由被告承担。 原告对其主张事实在举证期限内提供的证据有：一、道路交通事故认定书，证明余生才在交通事故中受伤、桂01-G2242号拖拉机损坏的事实，被告韦少海承担事故的全部责任；二、出院记录、住院收费收据、住院费用清单、疾病证明书等，证明原告第二次住院治疗经过、支出的医疗费及住院期间需护理及出院后医嘱全休一个月的事实；三、户口薄、出生证、结婚证，证明原告的家庭组成情况；四、广西科桂司法鉴定中心司法鉴定意见书、鉴定费发票，证明原告因交通事故受伤造成的伤残等级及支出的鉴定费700元；五、保险单，证明被告韦少海驾驶的车辆的投保情况；六、中国人民财产保险股份有限公司机动车保险车辆损失情况确认书，证明原告车辆的损失情况；七、货损发票，证明原告驾驶的车辆上货物的受损情况；八、（2013）武民初字第306号民事判决书，证明武宣县人民法院已就部分医疗费、误工费等进行判决；九、电脑咨询单，证明被告中财保柳州分公司的主体资格；十、劳动能力鉴定书及鉴定费，证明原告丧失劳动能力的情况，作该鉴定支出鉴定费700元；十一、宾阳县公安局新桥派出所亲属关系证明，证明余生才的父母生育子女情况。经质证，被告中财保柳州分公司对原告提供的证据有如下异议：一、证据二中三张门诊费用无相关的病历证实该门诊费用支出与此次交通事故有关；二、事故发生时间为2012年11月20日，而原告提供的货损发票开具日期为2015年7月27日，相距的时间较长，且发票载明的收款人为余生才，余生才不是付款人，不能证明该发票与原告货损有关，且交警出具的交通事故认定书中并未载明原告所载货物损失；三、原告经鉴定为十级伤残，而原告提供的劳动能力鉴定意见书鉴定原告的伤残等级为六级，鉴定结论不具有可塑性，对原告丧失劳动能力的鉴定结论不认可；四、对原告提供的其他证据无异议。被告韦少海、陈世刚对原告提供的证据的质证意见与被告中财保柳州分公司的意见一致。 被告韦少海辩称，其驾驶的车辆已在被告中财保柳州分公司购买了保险，原告的损失应由保险公司进行赔偿。 被告陈世刚辩称，其所有的桂B×××××号车已在被告中财保柳州分公司投保了交强险及商业第三者责任险，原告的损失应当由保险公司代其赔偿。 被告中财保柳州分公司辩称，一、保险公司对交警部门出具的交通事故认定书所认定的事故事实及责任划分没有异议。二、事故车辆桂B×××××号车在中财保柳州分公司投保交强险及商业第三者责任险，事故发生在保险期限内，对原告合理合法的损失，保险公司愿意在交强险赔偿限额内先行赔偿，不足部分在商业第三者责任险责任限额内赔偿，对超出保险责任范围内的赔偿由韦少海、陈世刚自行承担赔偿责任。三、（2013）武民初字第306号判决书判决中财保柳州分公司在交强险限额内赔偿原告36394．91元（其中医药费10000元），在商业第三者险限额内赔偿11108．24元，负担诉讼费409元，中财保柳州分公司已履行完判决内容；四、原告部分请求不合理，计算方法不正确。医药费按票据应为6799．88元，扣除乙类用药789．81元，保险公司认可6010．07元，门诊费用266．3元没有病历佐证，不认可。残疾赔偿金应按20年计算，乘以18％的系数，为27234元。护理费因无医嘱需护理，不认可，即使存在护理费亦应参照误工费计算，为675．9元。交通费、住宿费无证据证明，不予认可。住院伙食补助费没有异议。营养费因无医嘱需增加营养，不予认可。因原告未完全丧失劳动能力，其主张的被扶养人生活费不予认可，如要计算被扶养人生活费，因原告有多个被扶养人，因此，被扶养人生活费不得超过上一年度人均年消费支出总额。车辆损失费定损为9545元，残值500元，实际车损应为9045元。货物损失费因原告无法提供证据证明存在货物损失，事故认定书亦未载明有货物损失，不予认可。 被告韦少海、陈世刚、中财保柳州分公司均未提供证据。 根据原、被告双方诉辩意见，本院归纳本案的争议焦点为：原告的各项诉讼请求是否有事实和法律依据。 对原、被告提供的证据本院确认如下： 一、原告提供的道路交通事故认定书、出院记录、住院收费收据、住院费用清单、疾病证明书、户口薄、出生证、结婚证、广西科桂司法鉴定中心司法鉴定意见书及鉴定费发票、保险单、中国人民财产保险股份有限公司机动车保险车辆损失情况确认书、（2013）武民初字第306号民事判决书、电脑咨询单、宾阳县公安局新桥派出所亲属关系证明等证据原、被告双方均无异议，本院予以采纳。 二、原告提供的三张门诊收费收据，因无其他病历资料证实该项支出是治疗原告因交通事故造成的伤情，不予采纳。 三、原告提交的货损发票因无其他证据证实与本案具有关联性，不予采纳。 四、原告提交的广西科桂司法鉴定中心劳动能力鉴定意见书系依据国家标准GB／T16180-1996《职工工伤与职业病致残程度鉴定》作出，该鉴定结论是作为劳动者请求工伤保险待遇的依据，与本案不具有关联性，不予采纳。")
    len = len(cut)
    for i in range(0, len):
        jieba_sum += cut[i]["jieba_overlap"]
        thulac_sum += cut[i]["thulac_overlap"]
        print("origin: " + cut[i]["sentence"])
        print("result: " + str(cut[i]["result"]))
        print("jieba:  " + str(cut[i]["jieba"]) + "  " + str(cut[i]["jieba_overlap"]))
        print("thulac: " + str(cut[i]["thulac"]) + "  " + str(cut[i]["thulac_overlap"]))
        print()
    print("jieba:" + str(jieba_sum/len)+"  thulac:" + str(thulac_sum/len))