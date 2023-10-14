import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import HeatMap

# Create a base map centered around Kuala Lumpur
m = folium.Map(location=[3.1390, 101.6869], zoom_start=12)

# Your list of latitudes and longitudes
data = {'The Flow Studio': [
    [3.1277706972688635, 101.67439875621255],
    [3.1519383363602462, 101.66553696882904],
    [3.138249, 101.63008],
    [3.052161, 101.671278]
    ],
    'karma yoga': [
        [3.1323484914363386, 101.67129709581177]
        ],
    'Life Hot Yoga': [
        [3.149766037831857, 101.59387235348427],
        [3.167091133373805, 101.65190068232039]
        ],
    'Celebrity Fitness': [
        [3.130551466205832, 101.67138542279474],
        [3.1512698118957534, 101.6169901603],
        [3.0698452683269846, 101.69535177114773],
        [3.1193243119004923, 101.67848784897004],
        [3.1958333217962744, 101.63381297508522]
        ],
    'Urban Spring Pilates': [
        [3.1384434073561533, 101.6688006580661],
        [3.1682057077947823, 101.65239181115658]
        ],
    'AlignYoga': [
        [3.052142720526545, 101.67918610039212]
        ],
    'Surya Yoga': [
        [3.1300817056560275, 101.59657197017448],
        [3.078323903350539, 101.69372597375367],
        [3.0927007030010296, 101.68761344990328],
        [3.0457372128617792, 101.62267624933123],
        [3.010448265835054, 101.53854430327854],
        [3.0978648832843207, 101.75346413257392],
        [3.017641745178442, 101.69612923218372]
        ],
    'Simplylife Yoga': [
        [3.179423396637816, 101.68323264272207]
        ],
    'YU+ Studio': [
        [3.0543866096330508, 101.67000526697564],
        [3.036385337758758, 101.76508320930336]
        ],
    'Omsphere': [
        [3.0531466874387894, 101.73909438046711]
        ],
    'Mysore Room': [
        [3.171403844928022, 101.66593865348423]
        ],
    'Sanctum Wellness at EQ': [
        [3.153035935376106, 101.7097521093033]
        ],
    'mYoga': [
        [3.1285862842180845, 101.71357731573829]
        ],
    'Art Printing Works Yoga': [
        [3.1244613625431485, 101.67427181573822]
        ],
    'Damai Studio and Cafe': [
        [3.1662218740184365, 101.71750229581187]
        ],
    'Life n Fitness': [
        [3.12873404090602, 101.63503775348423],
        [3.095408586930257, 101.73852216697564],
        [3.1408348512615536, 101.70754993813944]
        ],
    'Journey Within Studio': [
        [3.1550800734689615, 101.59488056882898]
        ],
    'Yogic Spandana': [
        [3.16200592618416, 101.74212885991994]
        ]
    }

regions = {'Bangsar': [
    (3.1277706972688635, 101.67439875621255),
    (3.1323484914363386, 101.67129709581177),
    (3.130551466205832, 101.67138542279474),
    (3.1384434073561533, 101.6688006580661)
    ],
    'Damansara Heights': [
        (3.1519383363602462, 101.66553696882904),
        (3.149766037831857, 101.59387235348427),
        (3.1512698118957534, 101.6169901603),
        (3.1300817056560275, 101.59657197017448),
        (3.12873404090602, 101.63503775348423),
        (3.1550800734689615, 101.59488056882898)],
    'TTDI': [
        (3.138249, 101.63008)
        ],
    'Bukit Jalil': [
        (3.052161, 101.671278),
        (3.0698452683269846, 101.69535177114773),
        (3.052142720526545, 101.67918610039212),
        (3.078323903350539, 101.69372597375367),
        (3.0543866096330508, 101.67000526697564)
        ],
    'Mont Kiara': [
        (3.167091133373805, 101.65190068232039),
        (3.1682057077947823, 101.65239181115658),
        (3.171403844928022, 101.66593865348423)
        ],
    'Mid-Valley': [
        (3.1193243119004923, 101.67848784897004),
        (3.0927007030010296, 101.68761344990328),
        (3.1285862842180845, 101.71357731573829),
        (3.1244613625431485, 101.67427181573822)
        ],
    'Kepong Village': [
        (3.1958333217962744, 101.63381297508522)
        ],
    'Buchong Jaya': [
        (3.0457372128617792, 101.62267624933123)
        ],
    'Kota Kemuning': [
        (3.010448265835054, 101.53854430327854)
        ],
    'Cheras': [
        (3.0978648832843207, 101.75346413257392),
        (3.036385337758758, 101.76508320930336),
        (3.0531466874387894, 101.73909438046711),
        (3.095408586930257, 101.73852216697564)],
    'Seri Kembandang': [
        (3.017641745178442, 101.69612923218372)
        ],
    'Jalan Ipoh': [
        (3.179423396637816, 101.68323264272207)
        ],
    'Bukit Bintang': [
        (3.153035935376106, 101.7097521093033),
        (3.1662218740184365, 101.71750229581187),
        (3.1408348512615536, 101.70754993813944),
        (3.16200592618416, 101.74212885991994)
        ]
    }

# Create two columns. The first one for the toggle and selections, the second one for the map.
col1, col2 = st.columns(2)

# Radio button for Studios vs. Regions in the first column
selection_type = col1.radio("Select by:", ["Studios", "Regions"])

if selection_type == "Studios":
    # Implementing the "Select All" checkbox for studios in the first column
    select_all = col1.checkbox("Select all Studios")
    if select_all:
        selections = list(data.keys())
    else:
        selections = col1.multiselect("Which Yoga Studio do you want to see?", list(data.keys()))

    # Combine data from all selected studios into a single list and add markers with popups
    combined_data = []
    for s in selections:
        combined_data.extend(data[s])
        for point in data[s]:
            folium.CircleMarker(
                location=point,
                radius=6,
                color="rgba(255, 255, 255, 0)",
                fill=True,
                fill_color="rgba(255, 255, 255, 0)",
                fill_opacity=0,
                popup=s
            ).add_to(m)

else:
    # Implementing the "Select All" checkbox for regions in the first column
    select_all = col1.checkbox("Select all Regions")
    if select_all:
        selections = list(regions.keys())
    else:
        selections = col1.multiselect("Which Region do you want to see?", list(regions.keys()))

    # Combine data from all selected regions into a single list and add markers with popups
    combined_data = []
    for r in selections:
        combined_data.extend(regions[r])
        for point in regions[r]:
            folium.CircleMarker(
                location=point,
                radius=6,
                color="rgba(255, 255, 255, 0)",
                fill=True,
                fill_color="rgba(255, 255, 255, 0)",
                fill_opacity=0,
                popup=r
            ).add_to(m)

# Add a single heatmap to the base map using the combined data
HeatMap(combined_data).add_to(m)

# Display the map in the second column
# Convert the Folium map to an HTML string
html = m._repr_html_()

# Use the column's write function to display the map
col2.write(html, unsafe_allow_html=True)