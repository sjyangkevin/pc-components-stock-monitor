from collections import OrderedDict
from flask import Blueprint, render_template, current_app, request, redirect, url_for
from flaskr.db import get_db

from flaskr.form import FilterForm

bp = Blueprint('index', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():

    form = FilterForm()
    args = ''
    source_bestbuy = request.args.get('source_bestbuy', False, type=bool)
    source_canadacomputers = request.args.get('source_canadacomputers', False, type=bool)
    source_newegg = request.args.get('source_newegg', False, type=bool)
    GeForce_RTX_4090 = request.args.get('GeForce_RTX_4090', False, type=bool)
    GeForce_RTX_4080 = request.args.get('GeForce_RTX_4080', False, type=bool)
    GeForce_RTX_3090 = request.args.get('GeForce_RTX_3090', False, type=bool)
    GeForce_RTX_3080_Ti = request.args.get('GeForce_RTX_3080_Ti', False, type=bool)
    GeForce_RTX_3080 = request.args.get('GeForce_RTX_3080', False, type=bool)
    GeForce_RTX_3070_Ti = request.args.get('GeForce_RTX_3070_Ti', False, type=bool)
    GeForce_RTX_3070 = request.args.get('GeForce_RTX_3070', False, type=bool)
    GeForce_RTX_3060_Ti = request.args.get('GeForce_RTX_3060_Ti', False, type=bool)
    GeForce_RTX_3060 = request.args.get('GeForce_RTX_3060', False, type=bool)
    GeForce_RTX_3050 = request.args.get('GeForce_RTX_3050', False, type=bool)
    GeForce_RTX_2060_Super = request.args.get('GeForce_RTX_2060_Super', False, type=bool)
    GeForce_RTX_2060 = request.args.get('GeForce_RTX_2060', False, type=bool)
    GeForce_GTX_1660_Ti = request.args.get('GeForce_GTX_1660_Ti', False, type=bool)
    GeForce_GTX_1660_Super = request.args.get('GeForce_GTX_1660_Super', False, type=bool)
    GeForce_GTX_1660 = request.args.get('GeForce_GTX_1660', False, type=bool)
    GeForce_GTX_1650_Super = request.args.get('GeForce_GTX_1650_Super', False, type=bool)
    GeForce_GTX_1650 = request.args.get('GeForce_GTX_1650', False, type=bool)
    GeForce_GTX_1000_Series = request.args.get('GeForce_GTX_1000_Series', False, type=bool)
    Radeon_RX_7900_XTX = request.args.get('Radeon_RX_7900_XTX', False, type=bool)
    Radeon_RX_6900_6950_XT = request.args.get('Radeon_RX_6900_6950_XT', False, type=bool)
    Radeon_RX_6800_XT = request.args.get('Radeon_RX_6800_XT', False, type=bool)
    Radeon_RX_6800 = request.args.get('Radeon_RX_6800', False, type=bool)
    Radeon_RX_6700_6750_XT = request.args.get('Radeon_RX_6700_6750_XT', False, type=bool)
    Radeon_RX_6600_6650_XT = request.args.get('Radeon_RX_6600_6650_XT', False, type=bool)
    Radeon_RX_6600 = request.args.get('Radeon_RX_6600', False, type=bool)
    Radeon_RX_6500_XT = request.args.get('Radeon_RX_6500_XT', False, type=bool)
    ASRock = request.args.get('ASRock', False, type=bool)
    ASUS = request.args.get('ASUS', False, type=bool)
    CornElectronics = request.args.get('CornElectronics', False, type=bool)
    EVGA = request.args.get('EVGA', False, type=bool)
    GIGABYTE = request.args.get('GIGABYTE', False, type=bool)
    HP = request.args.get('HP', False, type=bool)
    INTEL = request.args.get('INTEL', False, type=bool)
    MAXSUN = request.args.get('MAXSUN', False, type=bool)
    MSI = request.args.get('MSI', False, type=bool)
    NVIDIA = request.args.get('NVIDIA', False, type=bool)
    PNY = request.args.get('PNY', False, type=bool)
    SAPPHIRE = request.args.get('SAPPHIRE', False, type=bool)
    VisionTek = request.args.get('VisionTek', False, type=bool)
    ZOTAC = request.args.get('ZOTAC', False, type=bool)
    POWERCOLOR = request.args.get('POWERCOLOR', False, type=bool)
    NVIDIA = request.args.get('NVIDIA', False, type=bool)
    yeston = request.args.get('yeston', False, type=bool)

    if request.method == 'POST':
        if form.validate_on_submit():
            source_bestbuy = form.source_bestbuy.data
            source_canadacomputers = form.source_canadacomputers.data
            source_newegg = form.source_newegg.data
            GeForce_RTX_4090 = form.GeForce_RTX_4090.data
            GeForce_RTX_4080 = form.GeForce_RTX_4080.data
            GeForce_RTX_3090 = form.GeForce_RTX_3090.data
            GeForce_RTX_3080_Ti = form.GeForce_RTX_3080_Ti.data
            GeForce_RTX_3080 = form.GeForce_RTX_3080.data
            GeForce_RTX_3070_Ti = form.GeForce_RTX_3070_Ti.data
            GeForce_RTX_3070 = form.GeForce_RTX_3070.data
            GeForce_RTX_3060_Ti = form.GeForce_RTX_3060_Ti.data
            GeForce_RTX_3060 = form.GeForce_RTX_3060.data
            GeForce_RTX_3050 = form.GeForce_RTX_3050.data
            GeForce_RTX_2060_Super = form.GeForce_RTX_2060_Super.data
            GeForce_RTX_2060 = form.GeForce_RTX_2060.data
            GeForce_GTX_1660_Ti = form.GeForce_GTX_1660_Ti.data
            GeForce_GTX_1660_Super = form.GeForce_GTX_1660_Super.data
            GeForce_GTX_1660 = form.GeForce_GTX_1660.data
            GeForce_GTX_1650_Super = form.GeForce_GTX_1650_Super.data
            GeForce_GTX_1650 = form.GeForce_GTX_1650.data
            GeForce_GTX_1000_Series = form.GeForce_GTX_1000_Series.data
            Radeon_RX_7900_XTX = form.Radeon_RX_7900_XTX.data
            Radeon_RX_6900_6950_XT = form.Radeon_RX_6900_6950_XT.data
            Radeon_RX_6800_XT = form.Radeon_RX_6800_XT.data
            Radeon_RX_6800 = form.Radeon_RX_6800.data
            Radeon_RX_6700_6750_XT = form.Radeon_RX_6700_6750_XT.data
            Radeon_RX_6600_6650_XT = form.Radeon_RX_6600_6650_XT.data
            Radeon_RX_6600 = form.Radeon_RX_6600.data
            Radeon_RX_6500_XT = form.Radeon_RX_6500_XT.data
            ASRock = form.ASRock.data
            ASUS = form.ASUS.data
            CornElectronics = form.CornElectronics.data
            EVGA = form.EVGA.data
            GIGABYTE = form.GIGABYTE.data
            HP = form.HP.data
            INTEL = form.INTEL.data
            MAXSUN = form.MAXSUN.data
            MSI = form.MSI.data
            NVIDIA = form.NVIDIA.data
            PNY = form.PNY.data
            SAPPHIRE = form.SAPPHIRE.data
            VisionTek = form.VisionTek.data
            ZOTAC = form.ZOTAC.data
            POWERCOLOR = form.POWERCOLOR.data
            NVIDIA = form.NVIDIA.data
            yeston = form.yeston.data
    
    if source_bestbuy:
        if args != '':
            args += '&'
        args += 'source_bestbuy={}'.format(source_bestbuy)
    if source_canadacomputers:
        if args != '':
            args += '&'
        args += 'source_canadacomputers={}'.format(source_canadacomputers)
    if source_newegg:
        if args != '':
            args += '&'
        args += 'source_newegg={}'.format(source_newegg)
    if GeForce_RTX_4090:
        if args != '':
            args += '&'
        args += 'GeForce_RTX_4090={}'.format(GeForce_RTX_4090)
    if GeForce_RTX_4080:
        if args != '':
            args += '&'
        args += 'GeForce_RTX_4080={}'.format(GeForce_RTX_4080)
    if GeForce_RTX_3090:
        if args != '':
            args += '&'
        args += 'GeForce_RTX_3090={}'.format(GeForce_RTX_3090)
    if GeForce_RTX_3080_Ti:
        if args != '':
            args += '&'
        args += 'GeForce_RTX_3080_Ti={}'.format(GeForce_RTX_3080_Ti)
    if GeForce_RTX_3080:
        if args != '':
            args += '&'
        args += 'GeForce_RTX_3080={}'.format(GeForce_RTX_3080)
    if GeForce_RTX_3070_Ti:
        if args != '':
            args += '&'
        args += 'GeForce_RTX_3070_Ti={}'.format(GeForce_RTX_3070_Ti)
    if GeForce_RTX_3070:
        if args != '':
            args += '&'
        args += 'GeForce_RTX_3070={}'.format(GeForce_RTX_3070)
    if GeForce_RTX_3060_Ti:
        if args != '':
            args += '&'
        args += 'GeForce_RTX_3060_Ti={}'.format(GeForce_RTX_3060_Ti)
    if GeForce_RTX_3060:
        if args != '':
            args += '&'
        args += 'GeForce_RTX_3060={}'.format(GeForce_RTX_3060)
    if GeForce_RTX_3050:
        if args != '':
            args += '&'
        args += 'GeForce_RTX_3050={}'.format(GeForce_RTX_3050)
    if GeForce_RTX_2060_Super:
        if args != '':
            args += '&'
        args += 'GeForce_RTX_2060_Super={}'.format(GeForce_RTX_2060_Super)
    if GeForce_RTX_2060:
        if args != '':
            args += '&'
        args += 'GeForce_RTX_2060={}'.format(GeForce_RTX_2060)
    if GeForce_GTX_1660_Ti:
        if args != '':
            args += '&'
        args += 'GeForce_GTX_1660_Ti={}'.format(GeForce_GTX_1660_Ti)
    if GeForce_GTX_1660_Super:
        if args != '':
            args += '&'
        args += 'GeForce_GTX_1660_Super={}'.format(GeForce_GTX_1660_Super)
    if GeForce_GTX_1660:
        if args != '':
            args += '&'
        args += 'GeForce_GTX_1660={}'.format(GeForce_GTX_1660)
    if GeForce_GTX_1650_Super:
        if args != '':
            args += '&'
        args += 'GeForce_GTX_1650_Super={}'.format(GeForce_GTX_1650_Super)
    if GeForce_GTX_1650:
        if args != '':
            args += '&'
        args += 'GeForce_GTX_1650={}'.format(GeForce_GTX_1650)
    if GeForce_GTX_1000_Series:
        if args != '':
            args += '&'
        args += 'GeForce_GTX_1000_Series={}'.format(GeForce_GTX_1000_Series)
    if Radeon_RX_7900_XTX:
        if args != '':
            args += '&'
        args += 'Radeon_RX_7900_XTX={}'.format(Radeon_RX_7900_XTX)
    if Radeon_RX_6900_6950_XT:
        if args != '':
            args += '&'
        args += 'Radeon_RX_6900_6950_XT={}'.format(Radeon_RX_6900_6950_XT)
    if Radeon_RX_6800_XT:
        if args != '':
            args += '&'
        args += 'Radeon_RX_6800_XT={}'.format(Radeon_RX_6800_XT)
    if Radeon_RX_6800:
        if args != '':
            args += '&'
        args += 'Radeon_RX_6800={}'.format(Radeon_RX_6800)
    if Radeon_RX_6700_6750_XT:
        if args != '':
            args += '&'
        args += 'Radeon_RX_6700_6750_XT={}'.format(Radeon_RX_6700_6750_XT)
    if Radeon_RX_6600_6650_XT:
        if args != '':
            args += '&'
        args += 'Radeon_RX_6600_6650_XT={}'.format(Radeon_RX_6600_6650_XT)
    if Radeon_RX_6600:
        if args != '':
            args += '&'
        args += 'Radeon_RX_6600={}'.format(Radeon_RX_6600)
    if Radeon_RX_6500_XT:
        if args != '':
            args += '&'
        args += 'Radeon_RX_6500_XT={}'.format(Radeon_RX_6500_XT)
    if ASRock:
        if args !='':
            args += '&'
        args += 'ASRock={}'.format(ASRock)
    if ASUS:
        if args !='':
            args += '&'
        args += 'ASUS={}'.format(ASUS)
    if CornElectronics:
        if args !='':
            args += '&'
        args += 'CornElectronics={}'.format(CornElectronics)
    if EVGA:
        if args !='':
            args += '&'
        args += 'EVGA={}'.format(EVGA)
    if GIGABYTE:
        if args !='':
            args += '&'
        args += 'GIGABYTE={}'.format(GIGABYTE)
    if HP:
        if args !='':
            args += '&'
        args += 'HP={}'.format(HP)
    if INTEL:
        if args !='':
            args += '&'
        args += 'INTEL={}'.format(INTEL)
    if MAXSUN:
        if args !='':
            args += '&'
        args += 'MAXSUN={}'.format(MAXSUN)
    if MSI:
        if args !='':
            args += '&'
        args += 'MSI={}'.format(MSI)
    if NVIDIA:
        if args !='':
            args += '&'
        args += 'NVIDIA={}'.format(NVIDIA)
    if PNY:
        if args !='':
            args += '&'
        args += 'PNY={}'.format(PNY)
    if SAPPHIRE:
        if args !='':
            args += '&'
        args += 'SAPPHIRE={}'.format(SAPPHIRE)
    if VisionTek:
        if args !='':
            args += '&'
        args += 'VisionTek={}'.format(VisionTek)
    if ZOTAC:
        if args !='':
            args += '&'
        args += 'ZOTAC={}'.format(ZOTAC)
    if POWERCOLOR:
        if args !='':
            args += '&'
        args += 'POWERCOLOR={}'.format(POWERCOLOR)
    if NVIDIA:
        if args !='':
            args += '&'
        args += 'NVIDIA={}'.format(NVIDIA)
    if yeston:
        if args !='':
            args += '&'
        args += 'yeston={}'.format(yeston)
    
    if request.method == 'POST':
        return redirect("{}?{}".format(url_for("index.index"), args))

    client   = get_db()
    db       = client[current_app.config.get('MONGO_DATABASE')]
    products = db['products']

    if request.method == 'GET':

        query = OrderedDict(
            [('$and', [])]
        )

        source_filter = {'source': {'$in': []}}
        type_filter   = {'$or': []}
        manufacturer_filter = {'$or': []}

        if source_bestbuy:
            form.source_bestbuy.data = source_bestbuy
            source_filter['source']["$in"].append('bestbuy')
        if source_canadacomputers:
            form.source_canadacomputers.data = source_canadacomputers
            source_filter['source']["$in"].append('canadacomputers')
        if source_newegg:
            form.source_newegg.data = source_newegg
            source_filter['source']["$in"].append('newegg')
        if GeForce_RTX_4090:
            form.GeForce_RTX_4090.data = GeForce_RTX_4090
            type_filter['$or'].append({'name': {'$regex':'GeForce RTX 4090'}})
        if GeForce_RTX_4080:
            form.GeForce_RTX_4080.data = GeForce_RTX_4080
            type_filter['$or'].append({'name': {'$regex':'GeForce RTX 4080'}})
        if GeForce_RTX_3090:
            form.GeForce_RTX_3090.data = GeForce_RTX_3090
            type_filter['$or'].append({'name': {'$regex':'GeForce RTX 3090'}})
        if GeForce_RTX_3080_Ti:
            form.GeForce_RTX_3080_Ti.data = GeForce_RTX_3080_Ti
            type_filter['$or'].append({'name': {'$regex':'GeForce RTX 3080 Ti'}})
        if GeForce_RTX_3080:
            form.GeForce_RTX_3080.data = GeForce_RTX_3080
            type_filter['$or'].append({'name': {'$regex':'GeForce RTX 3080'}})
        if GeForce_RTX_3070_Ti:
            form.GeForce_RTX_3070_Ti.data = GeForce_RTX_3070_Ti
            type_filter['$or'].append({'name': {'$regex':'GeForce RTX 3070 Ti'}})
        if GeForce_RTX_3070:
            form.GeForce_RTX_3070.data = GeForce_RTX_3070
            type_filter['$or'].append({'name': {'$regex':'GeForce RTX 3070'}})
        if GeForce_RTX_3060_Ti:
            form.GeForce_RTX_3060_Ti.data = GeForce_RTX_3060_Ti
            type_filter['$or'].append({'name': {'$regex':'GeForce RTX 3060 Ti'}})
        if GeForce_RTX_3060:
            form.GeForce_RTX_3060.data = GeForce_RTX_3060
            type_filter['$or'].append({'name': {'$regex':'GeForce RTX 3060'}})
        if GeForce_RTX_3050:
            form.GeForce_RTX_3050.data = GeForce_RTX_3050
            type_filter['$or'].append({'name': {'$regex':'GeForce RTX 3050'}})
        if GeForce_RTX_2060_Super:
            form.GeForce_RTX_2060_Super.data = GeForce_RTX_2060_Super
            type_filter['$or'].append({'name': {'$regex':'GeForce RTX 2060 Super'}})
        if GeForce_RTX_2060:
            form.GeForce_RTX_2060.data = GeForce_RTX_2060
            type_filter['$or'].append({'name': {'$regex':'GeForce RTX 2060'}})
        if GeForce_GTX_1660_Ti:
            form.GeForce_GTX_1660_Ti.data = GeForce_GTX_1660_Ti
            type_filter['$or'].append({'name': {'$regex':'GeForce GTX 1660 Ti'}})
        if GeForce_GTX_1660_Super:
            form.GeForce_GTX_1660_Super.data = GeForce_GTX_1660_Super
            type_filter['$or'].append({'name': {'$regex':'GeForce GTX 1660 Super'}})
        if GeForce_GTX_1660:
            form.GeForce_GTX_1660.data = GeForce_GTX_1660
            type_filter['$or'].append({'name': {'$regex':'GeForce GTX 1660'}})
        if GeForce_GTX_1650_Super:
            form.GeForce_GTX_1650_Super.data = GeForce_GTX_1650_Super
            type_filter['$or'].append({'name': {'$regex':'GeForce GTX 1650 Super'}})
        if GeForce_GTX_1650:
            form.GeForce_GTX_1650.data = GeForce_GTX_1650
            type_filter['$or'].append({'name': {'$regex':'GeForce GTX 1650'}})
        if GeForce_GTX_1000_Series:
            form.GeForce_GTX_1000_Series.data = GeForce_GTX_1000_Series
            type_filter['$or'].append({'name': {'$regex':'GeForce GTX 1'}})
        if Radeon_RX_7900_XTX:
            form.Radeon_RX_7900_XTX.data = Radeon_RX_7900_XTX
            type_filter['$or'].append({'name': {'$regex':'Radeon RX 7900 XTX'}})
        if Radeon_RX_6900_6950_XT:
            form.Radeon_RX_6900_6950_XT.data = Radeon_RX_6900_6950_XT
            type_filter['$or'].append({'name': {'$regex':'Radeon RX (6900|6950) XT'}})
        if Radeon_RX_6800_XT:
            form.Radeon_RX_6800_XT.data = Radeon_RX_6800_XT
            type_filter['$or'].append({'name': {'$regex':'Radeon RX 6800 XT'}})
        if Radeon_RX_6800:
            form.Radeon_RX_6800.data = Radeon_RX_6800
            type_filter['$or'].append({'name': {'$regex':'Radeon RX 6800'}})
        if Radeon_RX_6700_6750_XT:
            form.Radeon_RX_6700_6750_XT.data = Radeon_RX_6700_6750_XT
            type_filter['$or'].append({'name': {'$regex':'Radeon RX (6700|6750) XT'}})
        if Radeon_RX_6600_6650_XT:
            form.Radeon_RX_6600_6650_XT.data = Radeon_RX_6600_6650_XT
            type_filter['$or'].append({'name': {'$regex':'Radeon RX (6600|6650) XT'}})
        if Radeon_RX_6600:
            form.Radeon_RX_6600.data = Radeon_RX_6600
            type_filter['$or'].append({'name': {'$regex':'Radeon RX 6600'}})
        if Radeon_RX_6500_XT:
            form.Radeon_RX_6500_XT.data = Radeon_RX_6500_XT
            type_filter['$or'].append({'name': {'$regex':'Radeon RX 6500 XT'}})
        if ASRock:
            form.ASRock.data = ASRock
            manufacturer_filter['$or'].append({'name': {'$regex':'ASRock'}})
        if ASUS:
            form.ASUS.data = ASUS
            manufacturer_filter['$or'].append({'name': {'$regex':'ASUS'}})
        if CornElectronics:
            form.CornElectronics.data = CornElectronics
            manufacturer_filter['$or'].append({'name': {'$regex':'Corn Electronics'}})
        if EVGA:
            form.EVGA.data = EVGA
            manufacturer_filter['$or'].append({'name': {'$regex':'EVGA'}})
        if GIGABYTE:
            form.GIGABYTE.data = GIGABYTE
            manufacturer_filter['$or'].append({'name': {'$regex':'GIGABYTE'}})
        if HP:
            form.HP.data = HP
            manufacturer_filter['$or'].append({'name': {'$regex':'HP'}})
        if INTEL:
            form.INTEL.data = INTEL
            manufacturer_filter['$or'].append({'name': {'$regex':'INTEL'}})
        if MAXSUN:
            form.MAXSUN.data = MAXSUN
            manufacturer_filter['$or'].append({'name': {'$regex':'MAXSUN'}})
        if MSI:
            form.MSI.data = MSI
            manufacturer_filter['$or'].append({'name': {'$regex':'MSI'}})
        if NVIDIA:
            form.NVIDIA.data = NVIDIA
            manufacturer_filter['$or'].append({'name': {'$regex':'NVIDIA'}})
        if PNY:
            form.PNY.data = PNY
            manufacturer_filter['$or'].append({'name': {'$regex':'PNY'}})
        if SAPPHIRE:
            form.SAPPHIRE.data = SAPPHIRE
            manufacturer_filter['$or'].append({'name': {'$regex':'SAPPHIRE'}})
        if VisionTek:
            form.VisionTek.data = VisionTek
            manufacturer_filter['$or'].append({'name': {'$regex':'VisionTek'}})
        if ZOTAC:
            form.ZOTAC.data = ZOTAC
            manufacturer_filter['$or'].append({'name': {'$regex':'ZOTAC'}})
        if POWERCOLOR:
            form.POWERCOLOR.data = POWERCOLOR
            manufacturer_filter['$or'].append({'name': {'$regex':'POWERCOLOR'}})
        if yeston:
            form.yeston.data = yeston
            manufacturer_filter['$or'].append({'name': {'$regex':'yeston'}})

        if source_filter['source']['$in'] != []:
            query['$and'].append(source_filter)
        if type_filter['$or'] != []:
            query['$and'].append(type_filter)
        if manufacturer_filter['$or'] != []:
            query['$and'].append(manufacturer_filter)
        
        print(query)

        if query['$and'] == []:
            query = {}


    return render_template("index.html", products=products.find(query), form=form)
