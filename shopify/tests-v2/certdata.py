"""The testing pop-up's data, copied from the laboratory certificates:
   ALS Laboratories (UK) Ltd, TRTH2761684-1 (batch 0725022) and TRTH2761685-1 (batch 0725021), 22/07/2025
   M S Laboratories Ltd, report CR60146 (batches 0725021 and 0725022), 14 August 2025
   Where the two batches differ, the higher (worse) result is shown."""
TESTS=[
 ("Heavy metals","Lead (Pb)","Under 3 mg/kg","0.01 mg/kg","300× under the limit"),
 ("Heavy metals","Arsenic (As)","No legal limit for supplements","0.01 mg/kg",""),
 ("Heavy metals","Mercury (Hg)","Under 0.1 mg/kg","Under 0.01 mg/kg","Below what the lab can measure"),
 ("Heavy metals","Cadmium (Cd)","Under 1 mg/kg","Under 0.01 mg/kg","Below what the lab can measure"),
 ("Microbes","Salmonella","Not detected in 25g","Not detected",""),
 ("Microbes","E. coli","Under 10 cfu/g","Under 10 cfu/g",""),
 ("Microbes","Enterobacteria","Under 10,000 cfu/g","Under 10 cfu/g",""),
 ("Microbes","Total viable count","Under 500,000 cfu/g","10 cfu/g",""),
 ("Microbes","Yeasts","Under 10,000 cfu/g","Under 20 cfu/g",""),
 ("Microbes","Moulds","Under 10,000 cfu/g","Under 20 cfu/g",""),
]
CERTS=[
 ("ALS Laboratories (UK) Ltd","TRTH2761685-1","Microbiology, batch 0725021","22 Jul 2025"),
 ("ALS Laboratories (UK) Ltd","TRTH2761684-1","Microbiology, batch 0725022","22 Jul 2025"),
 ("M S Laboratories Ltd","CR60146","Heavy metals, batches 0725021 and 0725022","14 Aug 2025"),
]
SETTINGS={"batch":"0725021 · 0725022","doc_label":"Certificates of analysis","made":"","bbe":"","issued":"Jul–Aug 2025",
 "scope":"on two production batches","heading":"Every result came in within its limit.","stat_value":"300×","stat_label":"Under the lead limit",
 "chip":"No salmonella detected",
 "why_1_h":"Heavy metals",
 "why_1":"<p>Lead, arsenic, cadmium and mercury can build up in the body over time, and they can come in through plant extracts and minerals. Both batches were tested: lead came in at 0.01 mg/kg against a limit of 3, and mercury and cadmium were below what the lab can measure.</p>",
 "why_2_h":"Microbes",
 "why_2":"<p>Bacteria, yeasts and moulds can grow in ingredients that are stored or handled badly. Both batches were screened for six, including salmonella and E. coli. No salmonella was detected, and every other count was 20 per gram or under.</p>",
 "why_3_h":"Who tested it",
 "why_3":"<p>Microbiology was tested by ALS Laboratories (UK) Ltd and heavy metals by M S Laboratories Ltd, both independent UK laboratories. Every result here is copied from their certificates, listed with their numbers on the overview.</p>",
 "note":"Microbiology by ALS Laboratories (UK) Ltd, heavy metals by M S Laboratories Ltd, both independent UK labs. Where the two batches differed, the higher result is shown. Ask us for the certificates: hello@mutolongevity.com"}
def apply(sec):
    keep={k:v for k,v in sec['blocks'].items() if v['type']=='item'}
    order_items=[k for k in sec['block_order'] if k in keep]
    blocks={};order=[]
    for i,(lab,num,scope,date) in enumerate(CERTS,1):
        k=f"c{i:02d}";blocks[k]={"type":"cert","settings":{"lab":lab,"number":num,"scope":scope,"date":date}};order.append(k)
    for i,(g,n,spec,res,note) in enumerate(TESTS,1):
        k=f"t{i:02d}";blocks[k]={"type":"test","settings":{"group":g,"name":n,"spec":spec,"result":res,"note":note,"pass":True}};order.append(k)
    for k in order_items: blocks[k]=keep[k];order.append(k)
    sec['blocks']=blocks;sec['block_order']=order
    sec['settings'].update(SETTINGS)
    return sec
