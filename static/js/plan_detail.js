const primaryDetailsList = {
    "Empty": "",
    "Great Hall": "-100 Food production<br>+6 Public order<br>+25% Max number of all units in recruitment pool<br>Garrison",
    "Market": "-100 Food production<br>+6 Public order<br>+3 Supplies<br>+25% Income (Commerce)<br>Garrison",
    "Monastery": "-100 Food production<br>+8 Public order<br>+25% Income (Church)<br>Garrison",
    "Longphort": "-100 Food production<br>+6 Public order<br>+25% Max number of all units in recruitment pool<br>Garrison"
};

const secondaryDetailsList = {
    "Empty": "",
    "Benedictine Abbey": "+10 Public order<br>+100 Income (Church)<br>+1 Religious Estates",
    "Beach Port": "+3 Supplies<br>+135 Income (Commerce)<br>+60 Food<br>+6% Trade (factionwide)<br>+20% Income (Commerce)(all regions in adjacent provinces)",
    "Cloth": "+30 Clocth production<br>+230 Income (Commerce)<br>+40 Food production<br>+15% Income (Farm)(all regions in adjacent provinces)",
    "Copper": "+30 Copper production<br>-10 Public order<br>+425 Income (Industry)<br>-20% Construction cost for Industry buildings(all regions in adjacent provinces)",
    "Fishing": "+4 Supplies<br>+80 Income (Farm)<br>+85 Food Production<br>+40% Campaign movement range for navies (local sea region)<+1 Siege holdout time (local province)<br> +1 Siege attrition time for the region (local province)",
    "Farm": "+5 Supplies<br>+205 Income (Farm)<br>+105 Food production<br>+1 Agricultural Estates<br>+1 Siege holdout time (local province)",
    "Gold": "+30 Gold production<br>-7 Public order<br>+585 Income (Industry)<br>+15% Income (All)(all regions in adjacent provinces)",
    "Hunting": "+20 Furs production<br>+4 Supplies<br>+150 Income (Farm)<br>+80 Food production<br>+1 Agricultural Estates<br>-2 Turn until replenishment for missile infantry units in recruitment pool",
    "Iron": "+30 Iron production<br>-10 Public order<br>+445 Income (Industry)<br>-50% Construction cost for Garrison buildings (all regions in adjacent provinces)<br>-70% Upkeep for Garrison buildings (all regions in adjacent provinces)",
    "Lead": "+30 Lead production<br>-10 Public order<br>+340 Income (Industry)<br>-20% Construction for Monastery buildings (all regions in adjacent provinces)",
    "Orchard": "+5 Public order<br>+4 Supplies<br>+220 Income (Farm)<br>+90 Food production<br>+1 Agricultural Estates",
    "Pasture": "+5 Supplies<br>+125 Income (Farm)<br>+70 Food production<br>+1 Agricultural Estates<br>+1 Siege holdout time (local province)",
    "Pottery": "+30 Pottery production<br>+230 Income (Commerce)<br>+15% Income (Industry)(all regions in adjacent provinces)",
    "Salt": "+30 Salt production<br>-10 Public order<br>+4 Supplies<br>+115 Income (industry)<br>+130 Income (Commerce)<br>+50 Food production",
    "Silver": "+30 Silver production<br>-8 Public order<br>+555 Income (Industry)<br>-20% Construction cost for Mint and Martyr's Mint building chains (all regions)",
    "Tin": "+30 Tin production<br>-10 Public order<br>+280 Income (Industry)<br>+80% Income from Copper building chains (all regions)",
    "Wood": "+30 Timber production<br>-20% Construction cost (all region in adjacent provinces)<br>+300 Income (Industry)",
};

const tertiaryDetailsList = {
    "Empty": "",
    "Alehouse": "-30 Food production<br>+3 Public order<br>+280 Income (Commerce)<br>+3 Unit morale (armies in province)",
    "Arena": "-200 Income<br>+100 XP for units per turn<br>+100% Unit replenishment (multiplier)",
    "Artisans": "-30 Food production<br>+100% Income from Gold, Silver, Lead, and Tin building chains (local province)<br>+60% Income (Commerce)(local province)",
    "Bullaun": "-200 Income<br>+6 Public order<br>+15 Fame",
    "Church Crafts": "-30 Food production<br>+115 Income (Church)<br>+60% Income from Copper, Iron, Wood, and Lead building chains",
    "Church": "-300 Income<br>+6 Public order<br>+10 Fame<br>+100% Income (Church)",
    "Craft Merchant": "-30 Food production<br>+100% Income from Cloth, Pottery, and Salt building chains<br>+60% Income (Industry)",
    "Estate": "-30 Food production<br>+4 Public order<br>+3 Noble Estates",
    "Forge": "-350 Income<br>+20% Income (Industry)<br>Armour III: +15% armour<br>Weapons III: +15% Melee damage",
    "Garrison": "-300 Income<br>-50 Food production<br>+3 Public order<br>-50% Enemy campaign movement range (local enemy armies)<br>Provides garrison:<br>5 x Thegns<br>2 x Ceorl Archers",
    "Granary": "-250 Income<br>+4 Supplies<br>+70 Food production<br>+100% Unit replenishment<br>+2 Siege holdout time<br>+1 Siege attrition time for the region",
    "Herring Port": "+3 Supplies<br>+140 Income (Commerce)<br>+75 Food production",
    "Library": "-300 Income<br>-30 Food production<br>+3 Public order<br>+30% Research rate (factionwide)",
    "Market Fair": "-60 Food production<br>+315 Income (Commerce)<br>+20% Income from Market Fair building chains (all regions)",
    "Moot Hill": "-250 Income<br>-30 Food production<br>+3 Public order<br>+3 to faction Allegiance<br>-15% Corruption",
    "Mill": "-200 Income<br>+30% Fur production from all Hunting villages in this province<br>+30% Tradeable resource production from all industry villages in this province<br>+30% Food production from Farms, Pastures and Orchards (local province)<br>+30% Income (Farms)",
    "Merchant": "-30 Food production<br>+140 Income (Commerce)",
    "Mint": "-30 Food production<br>+235 Income (Commerce)<br>+15% Trade (factionwide)",
    "Port": "+4 Supplies<br>+20 Food production<br>+9% Trade (factionwide)",
    "Round Tower": "-100 Income<br>+3 Public order<br>+15 Fame<br>+60% Income (Church)",
    "Scribes": "-30 Food production<br>+3 Public order<br>+210 Income (Church)",
    "Tanner": "-30 Food production<br>+30% Fur production from all Hunting villages in this province (local province)<br>+30% Income (Commerce)",
    "Tithe Hall": "-4 Public order<br>+2 Siege holdout time<br>+60% Food production from Farms, Pastures and Orchards (local province)<br>+60% Income (Church)",
    "Tools": "-30 Food production<br>+60% Tradeable resource production from all industry villages in this province (local province)<br>+60% Income from Copper, Iron, and Wood building chains",
    "Trade Port": "-30 Food production<br>+10% Trade (factionwide)<br>+30% Fur production from all Hunting villages in this province (local province)<br>+15% Income (Commerce)(all regions in adjacent provinces)",
    "Viking Port": "+15 Fame<br>+110 Income (Commerce)<br>+45% Income (Commerce)(local province)<br>Armour III: +15% Armour<br>Weapons III: +15% Melee damage",
    "Warehouse": "+60% Food production from Port building chains (local province)<br>+100% Income from Port building chains",
    "Workshop": "-3 Public order<br>+205 Income (Industry)",
};

document.querySelector('#primary_building_details').innerHTML = primaryDetailsList[document.querySelector('#primary_building_image').alt];
document.querySelector('#secondary_building_1_details').innerHTML = secondaryDetailsList[document.querySelector('#secondary_building_1_image').alt];
document.querySelector('#secondary_building_2_details').innerHTML = secondaryDetailsList[document.querySelector('#secondary_building_2_image').alt];
document.querySelector('#secondary_building_3_details').innerHTML = secondaryDetailsList[document.querySelector('#secondary_building_3_image').alt];
document.querySelector('#tertiary_building_1_details').innerHTML = tertiaryDetailsList[document.querySelector('#tertiary_building_1_image').alt];
document.querySelector('#tertiary_building_2_details').innerHTML = tertiaryDetailsList[document.querySelector('#tertiary_building_2_image').alt];
document.querySelector('#tertiary_building_3_details').innerHTML = tertiaryDetailsList[document.querySelector('#tertiary_building_3_image').alt];
document.querySelector('#tertiary_building_4_details').innerHTML = tertiaryDetailsList[document.querySelector('#tertiary_building_4_image').alt];
document.querySelector('#tertiary_building_5_details').innerHTML = tertiaryDetailsList[document.querySelector('#tertiary_building_5_image').alt];