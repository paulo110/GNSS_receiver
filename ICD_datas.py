#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 19:42:11 2020

@author: paulbourgoin
"""

ICD_specifications = {
    "code_frequency": 10.23e6,
    "E5a":{
        "I":{
            "code_period" : 20e-3,
            "primary_code_lenght" : 10230,
            "secondary_code_lenght" : 20,
            "feedback_tap": {
                "register_1" : 0o40503,
                "register_2" : 0o50661
                }
            },
        "Q":{
            "code_period" : 100e-3,
            "primary_code_lenght" : 10230,
            "secondary_code_lenght" : 100,
            "feedback_tap": {
                "register_1" : 0o40503,
                "register_2" : 0o50661
                }
            }
        },
    "E5b":
        {
        "I": {
            "code_period" : 4e-3,
            "primary_code_lenght" : 10230,
            "secondary_code_lenght" : 4,
            "feedback_tap": {
                "register_1" : 0o64021,
                "register_2" : 0o51445
                }
            },
        "Q": {
            "code_period" : 100e-3,
            "primary_code_lenght" : 10230,
            "secondary_code_lenght" : 100,
            "feedback_tap" : {
                "register_1" : 0o64021,
                "register_2" : 0o43143
                }
            }
        }   
}


ICD_start_value_R1 = 0o77777
ICD_start_value_R2 = {
    "E5a" : {
        "I": {
            "1" : 0o30305,
            "2" : 0o14234,
            "3" : 0o27213,
            "4" : 0o20577,
            "5" : 0o23312,
            "6" : 0o33463,
            "7" : 0o15614,
            "8" : 0o12537,
            "9" : 0o01527,
            "10" : 0o30236,
            "11" : 0o27344,
            "12" : 0o07272,
            "13" : 0o36377,
            "14" : 0o17046,
            "15" : 0o06434,
            "16" : 0o15405,
            "17" : 0o24252,
            "18" : 0o11631,
            "19" : 0o24776,
            "20" : 0o00630,
            "21" : 0o11560,
            "22" : 0o17272,
            "23" : 0o27445,
            "24" : 0o31702,
            "25" : 0o13012,
            "26" : 0o14401,
            "27" : 0o34727,
            "28" : 0o22627,
            "29" : 0o30623,
            "30" : 0o27256,
            "31" : 0o01520,
            "32" : 0o14211,
            "33" : 0o31465,
            "34" : 0o22164,
            "35" : 0o33516,
            "36" : 0o02737,
            "37" : 0o21316,
            "38" : 0o35425,
            "39" : 0o35633,
            "40" : 0o24655,
            "41" : 0o14054,
            "42" : 0o27027,
            "43" : 0o06604,
            "44" : 0o31455,
            "45" : 0o34465,
            "46" : 0o25273,
            "47" : 0o20763,
            "48" : 0o31721,
            "49" : 0o17312,
            "50" : 0o13277            
            },
            
        "Q": {
            "1" : 0o25652,
            "2" : 0o05142,
            "3" : 0o24723,
            "4" : 0o31751,
            "5" : 0o27366,
            "6" : 0o24660,
            "7" : 0o33655,
            "8" : 0o27450,
            "9" : 0o07626,
            "10" : 0o01705,
            "11" : 0o12717,
            "12" : 0o32122,
            "13" : 0o16075,
            "14" : 0o16644,
            "15" : 0o37556,
            "16" : 0o02477,
            "17" : 0o02265,
            "18" : 0o06430,
            "19" : 0o25046,
            "20" : 0o12735,
            "21" : 0o04262,
            "22" : 0o11230,
            "23" : 0o00037,
            "24" : 0o06137,
            "25" : 0o04312,
            "26" : 0o20606,
            "27" : 0o11162,
            "28" : 0o22252,
            "29" : 0o30533,
            "30" : 0o24614,
            "31" : 0o07767,
            "32" : 0o32705,
            "33" : 0o05052,
            "34" : 0o27553,
            "35" : 0o03711,
            "36" : 0o02041,
            "37" : 0o34775,
            "38" : 0o05274,
            "39" : 0o37356,
            "40" : 0o16205,
            "41" : 0o36270,
            "42" : 0o06600,
            "43" : 0o26773,
            "44" : 0o17375,
            "45" : 0o35267,
            "46" : 0o36255,
            "47" : 0o12044,
            "48" : 0o26442,
            "49" : 0o21621,
            "50" : 0o25411  
            }
        },
    "E5b" : {
        "I": {
            "1" : 0o07220,
            "2" : 0o26047,
            "3" : 0o00252,
            "4" : 0o00252,
            "5" : 0o14161,
            "6" : 0o02540,
            "7" : 0o01537,
            "8" : 0o26023,
            "9" : 0o01725,
            "10" : 0o20637,
            "11" : 0o02364,
            "12" : 0o27731,
            "13" : 0o30640,
            "14" : 0o34174,
            "15" : 0o06464,
            "16" : 0o07676,
            "17" : 0o32231,
            "18" : 0o10353,
            "19" : 0o00755,
            "20" : 0o26077,
            "21" : 0o11644,
            "22" : 0o11537,
            "23" : 0o35115,
            "24" : 0o20452,
            "25" : 0o34645,
            "26" : 0o25664,
            "27" : 0o21403,
            "28" : 0o32253,
            "29" : 0o02337,
            "30" : 0o30777,
            "31" : 0o27122,
            "32" : 0o22377,
            "33" : 0o36175,
            "34" : 0o33075,
            "35" : 0o33151,
            "36" : 0o13134,
            "37" : 0o07433,
            "38" : 0o10216,
            "39" : 0o35466,
            "40" : 0o02533,
            "41" : 0o05351,
            "42" : 0o30121,
            "43" : 0o14010,
            "44" : 0o32576,
            "45" : 0o30326,
            "46" : 0o37433,
            "47" : 0o26022,
            "48" : 0o35770,
            "49" : 0o06670,
            "50" : 0o12017 
            },
            
        "Q": {
            "1" : 0o03331,
            "2" : 0o06143,
            "3" : 0o25322,
            "4" : 0o23371,
            "5" : 0o00413,
            "6" : 0o36235,
            "7" : 0o17750,
            "8" : 0o04745,
            "9" : 0o13005,
            "10" : 0o37140,
            "11" : 0o30155,
            "12" : 0o20237,
            "13" : 0o03461,
            "14" : 0o31662,
            "15" : 0o27146,
            "16" : 0o05547,
            "17" : 0o02456,
            "18" : 0o30013,
            "19" : 0o00322,
            "20" : 0o10761,
            "21" : 0o26767,
            "22" : 0o36004,
            "23" : 0o30713,
            "24" : 0o07662,
            "25" : 0o21610,
            "26" : 0o20134,
            "27" : 0o11262,
            "28" : 0o10706,
            "29" : 0o34143,
            "30" : 0o11051,
            "31" : 0o25460,
            "32" : 0o17665,
            "33" : 0o32354,
            "34" : 0o21230,
            "35" : 0o20146,
            "36" : 0o11362,
            "37" : 0o37246,
            "38" : 0o16344,
            "39" : 0o15034,
            "40" : 0o25471,
            "41" : 0o25646,
            "42" : 0o22157,
            "43" : 0o04336,
            "44" : 0o16356,
            "45" : 0o04075,
            "46" : 0o02626,
            "47" : 0o11706,
            "48" : 0o37011,
            "49" : 0o27041,
            "50" : 0o31024  
            }
        }
    }

ICD_secondary_code = {
    "CS4" : {
        "1" : 0x4
    },
    "CS20" : {
        "1" : 0x842E9
    },
    "CS25" : {
        "1" : 0x380AD90
    },
    "CS100" : {
        "1" : 0x83F6F69D8F6E15411FB8C9B1C,
        "2" : 0x66558BD3CE0C7792E83350525,
        "3" : 0x59A025A9C1AF0651B779A8381,
        "4" : 0xD3A32640782F7B18E4DF754B7,
        "5" : 0xB91FCAD7760C218FA59348A93,
        "6" : 0xBAC77E933A779140F094FBF98,
        "7" : 0x537785DE280927C6B58BA6776,
        "8" : 0xEFCAB4B65F38531ECA22257E2,
        "9" : 0x79F8CAE838475EA5584BEFC9B,
        "10" : 0xCA5170FEA3A810EC606B66494,
        "11" : 0x1FC32410652A2C49BD845E567,
        "12" : 0xFE0A9A7AFDAC44E42CB95D261,
        "13" : 0xB03062DC2B71995D5AD8B7DBE,
        "14" : 0xF6C398993F598E2DF4235D3D5,
        "15" : 0x1BB2FB8B5BF24395C2EF3C5A1,
        "16" : 0x2F920687D238CC7046EF6AFC9,
        "17" : 0x34163886FC4ED7F2A92EFDBB8,
        "18" : 0x66A872CE47833FB2DFD5625AD,
        "19" : 0x99D5A70162C920A4BB9DE1CA8,
        "20" : 0x81D71BD6E069A7ACCBEDC66CA,
        "21" : 0xA654524074A9E6780DB9D3EC6,
        "22" : 0xC3396A101BEDAF623CFC5BB37,
        "23" : 0xC3D4AB211DF36F2111F2141CD,
        "24" : 0x3DFF25EAE761739265AF145C1,
        "25" : 0x994909E0757D70CDE389102B5,
        "26" : 0xB938535522D119F40C25FDAEC,
        "27" : 0xC71AB549C0491537026B390B7,
        "28" : 0x0CDB8C9E7B53F55F5B0A0597B,
        "29" : 0x61C5FA252F1AF81144766494F,
        "30" : 0x626027778FD3C6BB4BAA7A59D,
        "31" : 0xE745412FF53DEBD03F1C9A633,
        "32" : 0x3592AC083F3175FA724639098,
        "33" : 0x52284D941C3DCAF2721DDB1FD,
        "34" : 0x73B3D8F0AD55DF4FE814ED890,
        "35" : 0x94BF16C83BD7462F6498E0282,
        "36" : 0xA8C3DE1AC668089B0B45B3579,
        "37" : 0xFFFFFFFFFFFFFFFFFFFFFFFFF,
        "38" : 0xFFFFFFFFFFFFFFFFFFFFFFFFF,
        "39" : 0xFFFFFFFFFFFFFFFFFFFFFFFFF,
        "40" : 0x22D6E2A768E5F35FFC8E01796,
        "41" : 0x25310A06675EB271F2A09EA1D,
        "42" : 0x9F7993C621D4BEC81A0535703,
        "43" : 0xD62999EACF1C99083C0B4A417,
        "44" : 0xF665A7EA441BAA4EA0D01078C,
        "45" : 0x46F3D3043F24CDEABD6F79543,
        "46" : 0xE2E3E8254616BD96CEFCA651A,
        "47" : 0xE548231A82F9A01A19DB5E1B2,
        "48" : 0x265C7F90A16F49EDE2AA706C8,
        "49" : 0x364A3A9EB0F0481DA0199D7EA,
        "50" : 0x9810A7A898961263A0F749F56,
        "51" : 0xCFF914EE3C6126A49FD5E5C94,
        "52" : 0xFC317C9A9BF8C6038B5CADAB3,
        "53" : 0xA2EAD74B6F9866E414393F239,
        "54" : 0x72F2B1180FA6B802CB84DF997,
        "55" : 0x13E3AE93BC52391D09E84A982,
        "56" : 0x77C04202B91B22C6D3469768E,
        "57" : 0xFEBC592DD7C69AB103D0BB29C,
        "58" : 0x0B494077E7C66FB6C51942A77,
        "59" : 0xDD0E321837A3D52169B7B577C,
        "60" : 0x43DEA90EA6C483E7990C3223F,
        "61" : 0x0366AB33F0167B6FA979DAE18,
        "62" : 0x99CCBBFAB1242CBE31E1BD52D,
        "63" : 0xA3466923CEFDF451EC0FCED22,
        "64" : 0x1A5271F22A6F9A8D76E79B7F0,
        "65" : 0x3204A6BB91B49D1A2D3857960,
        "66" : 0x32F83ADD43B599CBFB8628E5B,
        "67" : 0x3871FB0D89DB77553EB613CC1,
        "68" : 0x6A3CBDFF2D64D17E02773C645,
        "69" : 0x2BCD09889A1D7FC219F2EDE3B,
        "70" : 0x3E49467F4D4280B9942CD6F8C,
        "71" : 0x658E336DCFD9809F86D54A501,
        "72" : 0xED4284F345170CF77268C8584,
        "73" : 0x29ECCE910D832CAF15E3DF5D1,
        "74" : 0x456CCF7FE9353D50E87A708FA,
        "75" : 0xFB757CC9E18CBC02BF1B84B9A,
        "76" : 0x5686229A8D98224BC426BC7FC,
        "77" : 0x700A2D325EA14C4B7B7AA8338,
        "78" : 0x1210A330B4D3B507D854CBA3F,
        "79" : 0x438EE410BD2F7DBCDD85565BA,
        "80" : 0x4B9764CC455AE1F61F7DA432B,
        "81" : 0xBF1F45FDDA3594ACF3C4CC806,
        "82" : 0xDA425440FE8F6E2C11B8EC1A4,
        "83" : 0xEE2C8057A7C16999AFA33FED1,
        "84" : 0x2C8BD7D8395C61DFA96243491,
        "85" : 0x391E4BB6BC43E98150CDDCADA,
        "86" : 0x399F72A9EADB42C90C3ECF7F0,
        "87" : 0x93031FDEA588F88E83951270C,
        "88" : 0xBA8061462D873705E95D5CB37,
        "89" : 0xD24188F88544EB121E963FD34,
        "90" : 0xD5F6A8BB081D8F383825A4DCA,
        "91" : 0x0FA4A205F0D76088D08EAF267,
        "92" : 0x272E909FAEBC65215E263E258,
        "93" : 0x3370F35A674922828465FC816,
        "94" : 0x54EF96116D4A0C8DB0E07101F,
        "95" : 0xDE347C7B27FADC48EF1826A2B,
        "96" : 0x01B16ECA6FC343AE08C5B8944,
        "97" : 0x1854DB743500EE94D8FC768ED,
        "98" : 0x28E40C684C87370CD0597FAB4,
        "99" : 0x5E42C19717093353BCAAF4033,
        "100" : 0x64310BAD8EB5B36E38646AF01,
        }
}

ICD_secondary_code_choice = {
    "E5a":{
        "I":{},
        "Q":{}
    },
    "E5b":{
        "I":{},
        "Q":{}
    }
}

def transform_sec_code_right_lenght(number,lenght):
    """ Take in input the number value and transform it into the right lenght"""
    listBinValue = list(f"{number:0{lenght:d}b}")
    return [int(value) for value in listBinValue]

def fill_ICD_secondary_choice():
    for i in range(1,51):
        ICD_secondary_code_choice["E5a"]["I"][str(i)]=transform_sec_code_right_lenght(ICD_secondary_code["CS20"]["1"],ICD_specifications["E5a"]["I"]["secondary_code_lenght"])
        ICD_secondary_code_choice["E5a"]["Q"][str(i)]=transform_sec_code_right_lenght(ICD_secondary_code["CS100"][str(i)],ICD_specifications["E5a"]["Q"]["secondary_code_lenght"])
        ICD_secondary_code_choice["E5b"]["I"][str(i)]=transform_sec_code_right_lenght(ICD_secondary_code["CS4"]["1"],ICD_specifications["E5b"]["I"]["secondary_code_lenght"])
        ICD_secondary_code_choice["E5b"]["Q"][str(i)]=transform_sec_code_right_lenght(ICD_secondary_code["CS100"][str(i+50)],ICD_specifications["E5b"]["Q"]["secondary_code_lenght"])

fill_ICD_secondary_choice()







