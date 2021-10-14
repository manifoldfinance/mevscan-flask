INFURA_URL = "https://mainnet.infura.io/v3/51f84cc2f3374b388939ef48c00e87ac"
"""
@TODO
Add these following miner addresses:

2miners
4hash
crazypool
k1-pool
luxor
minerall
miningexpress
miningpoolhub
pandapool
solopool
viabtc
"""

MINERS = {
    "0xB7e390864a90b7b923C9f9310C6F98aafE43F707": "private_miner07",
    "0x2A0eEe948fBe9bd4B661AdEDba57425f753EA0f6": "666pool",
    "0x00192fb10df37c9fb26829eb2cc623cd1bf599e8": "2Miners: PPLNS",
    "0x002e08000acbbae2155fab7ac01929564949070d": "2Miners: SOLO",
    "0xc839ee5542b4e8413246b3634c5c739fea949562": "AlphaPool",
    "0xa855c20a1351acd2690c716e2709c7dff3978d12": "AntPool",
    "0xb3b7874f13387d44a3398d298b075b7a3505d8d4": "Babel Pool",
    "0xff1b891969773159366ab6310ff63a69ac4acffd": "BaikalMine 1",
    "0x4ff271d3e8298213be3d88d257f3973a4b6d727b": "Baypool",
    "0x99c85bb64564d9ef9a99621301f22c9993cb89e3": "BeePool",
    "0x01ca8a0ba4a80d12a8fb6e3655688f57b16608cf": "Binance, pool.binance.com",
    "0xf3b9d2c81f2b24b0fa0acaaa865b7d9ced5fc2fb": "BitClubPool",
    "0xeea5b82b61424df8020f5fedd81767f2d0d25bfb": "BTC.com Pool",
    "0x52e44f279f4203dcf680395379e5f9990a69f13c": "Bw Pool",
    "0x68795c4aa09d6f4ed3e5deddf8c2ad3049a601da": "CoinMine.pl",
    "0xf8b483dba2c3b7176a3da549ad41a48bb3121069": "Coinotron 1",
    "0xa42af2c70d316684e57aefcc6e393fecb1c7e84e": "Coinotron 2",
    "0x6a7a43be33ba930fe58f34e07d0ad6ba7adb9b1f": "Coinotron 3",
    "0xe5a349fc4ff853dfdd0b7eaaa9dcd8918e768f49": "CoolPool.Top: SOLO",
    "0x249bdb4499bd7c683664c149276c1d86108e2137": "Cruxpool",
    "0xcf0e04cc0b8fcd66f42679bce42bf2569f438234": "DigiPools",
    "0x2a65aca4d5fc5b5c859090a6c34d164135398226": "DwarfPool",
    "0x151255dd9e38e44db38ea06ec66d0d113d6cbe37": "DwarfPool 2",
    "0xc4aeb20798368c48b27280847e187bb332b9bc77": "Easy2Mine",
    "0xa027231f42c80ca4125b5cb962a21cd4f812e88f": "Eth.pp.ua",
    "0xf35074bbd0a9aee46f4ea137971feec024ab704e": "ETH.SoloPool.org",
    "0x8fce1ef27f3add1411c7a99be402de598ad38389": "EthashPool 1",
    "0x52f13e25754d822a3550d0b68fdefe9304d27ae8": "EthashPool 2",
    "0x8d35067233605bef6069191ae0922d134ff80d48": "EtherDig",
    "0x9d551f41fed6fc27b719777c224dfecce170004d": "EthereumPool",
    "0xea674fdde714fd979de3edf0f56aa9716b898ec8": "Ethermine",
    "0xe6a7a1d47ff21b6321162aea7c6cb457d5476bca": "Ethpool",
    "0x4bb96091ee9d802ed039c4d1a5f6216f90f81b01": "Ethpool 2",
    "0x6537b65a50a862391515455272f9b6c7168afe94": "ExtremeHash",
    "0xcc22cb1b6625b64e81909456111d76be6158dfbc": "EzilPool 1",
    "0x8595dd9e0438640b5e1254f9df579ac12a86865f": "EzilPool 2",
    "0xf20b338752976878754518183873602902360704": "F2Pool",
    "0x829bd824b016326a401d083b33d092293333a830": "F2Pool Old",
    "0x35f61dfb08ada13eba64bf156b80df3d5b3a738d": "firepool",
    "0xb6cf40aee9990c25d7d6193952af222e120b31c2": "FKPool",
    "0x7f101fe45e6649a6fb8f3f8b43ed03d353f2b90c": "Flexpool.io",
    "0xd34da389374caad1a048fbdc4569aae33fd5a375": "Genesis Mining",
    "0xd0db3c9cf4029bac5a9ed216cd174cba5dbf047c": "HashON Pool",
    "0x1ad91ee08f21be3de0ba2ba6918e714da6b45836": "Hiveon Pool",
    "0x1aD91ee08f21bE3dE0BA2ba6918E714dA6B45836": "Hiveon Pool2",
    "0x4c549990a7ef3fea8784406c1eecc98bf4211fa5": "Hiveon: Old Pool",
    "0x14b30f257c2737370203a15aa343c2b600dfb675": "Huixingpool.com",
    "0x9d6d492bd500da5b33cf95a5d610a73360fcaaa0": "Huobi Mining Pool",
    "0xf64f9720cfcb59ca4f5f45e6fdb3f68b875b7295": "ICanMining.ru",
    "0x433022c4066558e7a32d850f02d2da5ca782174d": "K1POOL.COM",
    "0x4e4e23ac3c11789e23169025503ea4373b01417b": "KuveraPool",
    "0x7f3b29ae0d5edae9bb148537d4ed2b12beddf8b3": "MATPool",
    "0x6c3183792fbb4a4dd276451af6baf5c66d5f5e48": "MaxHash: EthPool",
    "0xcf6ce585cb4a78a6f96e6c8722927161a696f337": "MaxHash: Solo Mining",
    "0x09ab1303d3ccaf5f018cd511146b07a240c70294": "Minerall Pool",
    "0xbbbbbbbb49459e69878219f906e73aa325ff2f0c": "Mining DAO: Block Producer",
    "0x06b8c5883ec71bc3f4b332081519f23834c8706e": "Mining Express",
    "0x3ecef08d0e2dad803847e052249bb4f8bff2d5bb": "MiningPoolHub",
    "0x2a98776c7e13ed1c240858bd241dcf95fc1928b4": "myminers.org: Solo",
    "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b": "Nanopool",
    "0x2f979c933aef4fcddd27c0fa5c54d8a780555b0a": "NEST Protocol: Mining Pool",
    "0xd5bbb4264b70ca4f58c45d27b9d7e11190754a54": "NoobPool",
    "0x6b7d50bb8fab584e54251a10e1c6cfa51dd7b618": "PandaPool",
    "0x47c439c8784b44366735fc2cfe08228cb91d5b8e": "PoolHub",
    "0xa7b0536fb02c593b0dfd82bd65aacbdd19ae4777": "Poolin1",
    "0xc8F595E2084DB484f8A80109101D58625223b7C9": "Poolin2",
    "0xe16263ee79b0ee32c242c99f02559e92abaea9eb": "SaturnPool",
    "0x5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c": "Spark Pool",
    "0x0708F87A089a91C65d48721Aa941084648562287": "SpiderPool",
    "0x1dcb8d1f0fcc8cbc8c2d76528e877f915e299fbe": "Suprnova",
    "0x63a9975ba31b0b9626b34300f7f627147df1f526": "Suprnova 2",
    "0xa3c084ae80a3f03963017669bc696e961d3ae5d5": "Uleypool",
    "0xd224ca0c819e8e97ba0136b3b95ceff503b79f53": "UUPool",
    "0x44fd3ab8381cc3d14afa7c4af7fd13cdc65026e1": "W POOL",
    "0x9435d50503aee35c8757ae4933f7a0ab56597805": "WaterholePool",
    "0xd1e56c2e765180aa0371928fd4d1e41fbcda34d4": "Weipool",
    "0x7c6694032b4db11ac485e1cff0f7509d58b41569": "Whalesburg Pool: Old Address",
    "0xe4bdced60430a90f31dba03524dd5d15a2670649": "xnpool.cn",
    "0x6a851246689eb8fc77a9bf68df5860f13f679fa0": "ZET Technologies",
    "0x04668ec2f57cc15c381b461b9fedab5d451c8f7f": "zhizhu.top",
}
