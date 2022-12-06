import comtypes.client as cc
import comtypes

def downIDM(link, path, name):
    referrer = ""
    cookie = ""
    postData = ""
    user = ""
    password = ""
    cc.GetModule(["{ECF21EAB-3AA8-4355-82BE-F777990001DD}",1,0])
    # not sure about the syntax here, but cc.GetModule will tell you the name of the wrapper it generated
    import comtypes.gen._ECF21EAB_3AA8_4355_82BE_F777990001DD_0_1_0 as IDMan
    idm1 = cc.CreateObject("IDMan.CIDMLinkTransmitter", None, None, IDMan.ICIDMLinkTransmitter2)
    idm1.SendLinkToIDM(link,
    referrer, cookie, postData, user, password, path, name, 2)
