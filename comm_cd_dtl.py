#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request

def get_dmn_met_info(comm_cd_id):
    url = "http://150.149.49.131:9003/ukeyMeta/meta/biz/std/dmn/ZDSTJSTS00100.jsp?cmbDMN_TYP_CD=003&sltINTEG_CD_NM=&sltTRM_SYS_MET_ID=TRS900000000001&sltDMN_HAN_NM=" + comm_cd_id
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    try:
        dmn_met_id = soup.find('dmn_met_id').string
        dmn_han_nm = soup.find('dmn_han_nm').string
        integ_cd_nm = soup.find('integ_cd_nm').string
    except AttributeError as e:
        print(e)
        dmn_met_id = ''
        dmn_han_nm = ''
        integ_cd_nm = ''
        
    return dmn_met_id, dmn_han_nm, integ_cd_nm

def get_instances(domain_id):
    url = "http://150.149.49.131:9003/ukeyMeta/meta/biz/std/dmn/tab/ZDSTJSTS00120.jsp?Type=0&DmnType=003&DmnId=" + domain_id
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    
    comm_cd_val_lst = [item.string for item in soup.find_all("nst_eng_nm")]
    
    print(comm_cd_val_lst)
    
if __name__ == '__main__':
    comm_cd_id_lst = ["svc_dtl_cl_cd", "svc_cd", "rdtn_cl_cd", "wlf_dc_cd"]
    
    for item in comm_cd_id_lst:
        domain_id, domain_nm, comm_cd_id = get_dmn_met_info(item)
    
        print(domain_id, domain_nm, comm_cd_id)
        
        get_instances(domain_id)
'''
1. 도메인명으로 조회
http://150.149.49.131:9003/ukeyMeta/meta/biz/std/dmn/ZDSTJSTS00100.jsp?cmbDMN_TYP_CD=003&sltDMN_HAN_NM=oss_svc_req_obj_cd&sltINTEG_CD_NM=&sltTRM_SYS_MET_ID=TRS900000000001

2. 컬럼 리스트 조회
http://150.149.49.131:9003/ukeyMeta/meta/biz/std/dmn/tab/ZDSTJSTS00120.jsp?Type=0&DmnId=DMN000000011340&DmnType=003
'''