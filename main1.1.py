import folium
from folium import plugins
from shapely.geometry import Polygon
from pyproj import Proj, transform

# Provided data
zone_data={
    "city": "Alappuzha Town",
    "zones": [
        {
            "id": 5,
            "name": "Alappuzha Town",
             "boundary": [
                {
                    "lat": 9.488462202837784,
                    "lng": 76.35800321805853
                },
                {
                    "lat": 9.523173773370845,
                    "lng": 76.35843814058593
                },
                {
                    "lat": 9.541091585477794,
                    "lng": 76.32991682578766
                },
                {
                    "lat": 9.524300628980985,
                    "lng": 76.3009738527257
                },
                {
                    "lat": 9.48960112843507,
                    "lng": 76.30054566781097
                },
                {
                    "lat": 9.471680514065769,
                    "lng": 76.32905372043156
                }
            ],
            "center_point": {
                "longitude": 76.32948857090007,
                "latitude": 9.506384972194708
            },
            
        },
        {
            "id": 6,
            "name": "Paravoor",
            "uber_h3_index_3km": 605173540148215807,
            "boundary": [
                {
                    "lat": 9.435814284802406,
                    "lng": 76.38608968046117
                },
                {
                    "lat": 9.47053047492161,
                    "lng": 76.38652782417839
                },
                {
                    "lat": 9.488462202837784,
                    "lng": 76.35800321805853
                },
                {
                    "lat": 9.471680514065769,
                    "lng": 76.32905372043156
                },
                {
                    "lat": 9.436976379090002,
                    "lng": 76.32862231615206
                },
                {
                    "lat": 9.419041877399508,
                    "lng": 76.35713367214326
                }
            ],
            "center_point": {
                "longitude": 76.35757173857083,
                "latitude": 9.453750955519512
            },
           
        },
        {
            "id": 7,
            "name": "Aaryad",
            "boundary": [
                {
                    "lat": 9.53996565950699,
                    "lng": 76.38740441313098
                },
                {
                    "lat": 9.574684603046311,
                    "lng": 76.38784285843536
                },
                {
                    "lat": 9.592599602814476,
                    "lng": 76.35930828495148
                },
                {
                    "lat": 9.57579847104058,
                    "lng": 76.3303485269322
                },
                {
                    "lat": 9.541091585477794,
                    "lng": 76.32991682578766
                },
                {
                    "lat": 9.523173773370845,
                    "lng": 76.35843814058593
                }
            ],
            "center_point": {
                "longitude": 76.35887650830394,
                "latitude": 9.557885615876165
            },
        },
        {
            "id": 8,
            "name": "Pathirapalli",
            "uber_h3_index_3km": 605173567931285503,
            "boundary": [
                {
                    "lat": 9.541091585477794,
                    "lng": 76.32991682578766
                },
                {
                    "lat": 9.57579847104058,
                    "lng": 76.3303485269322
                },
                {
                    "lat": 9.59370231568142,
                    "lng": 76.30183051714631
                },
                {
                    "lat": 9.576902105163171,
                    "lng": 76.27289408251386
                },
                {
                    "lat": 9.542207304348363,
                    "lng": 76.27246911714718
                },
                {
                    "lat": 9.524300628980985,
                    "lng": 76.3009738527257
                }
            ],
            "center_point": {
                "longitude": 76.30140548704215,
                "latitude": 9.559000401782052
            },
        },
        {
            "id": 13,
            "name": "Vaisyambhagom",
            "boundary": [
                {
                    "lat": 9.383147948645819,
                    "lng": 76.41417619949756
                },
                {
                    "lat": 9.417868692880182,
                    "lng": 76.41461756420702
                },
                {
                    "lat": 9.435814284802406,
                    "lng": 76.38608968046117
                },
                {
                    "lat": 9.419041877399508,
                    "lng": 76.35713367214326
                },
                {
                    "lat": 9.384333173382124,
                    "lng": 76.35669904868689
                },
                {
                    "lat": 9.366384836197081,
                    "lng": 76.38521369437225
                }
            ],
            "center_point": {
                "longitude": 76.38565497656136,
                "latitude": 9.40109846888452
            },
        },
        {
            "id": 12,
            "name": "Paravoor",
            "boundary": [
                {
                    "lat": 9.435814284802406,
                    "lng": 76.38608968046117
                },
                {
                    "lat": 9.47053047492161,
                    "lng": 76.38652782417839
                },
                {
                    "lat": 9.488462202837784,
                    "lng": 76.35800321805853
                },
                {
                    "lat": 9.471680514065769,
                    "lng": 76.32905372043156
                },
                {
                    "lat": 9.436976379090002,
                    "lng": 76.32862231615206
                },
                {
                    "lat": 9.419041877399508,
                    "lng": 76.35713367214326
                }
            ],
            "center_point": {
                "longitude": 76.35757173857083,
                "latitude": 9.453750955519512
            },
        },
        {
            "id": 11,
            "name": "Vandanam",
            "boundary": [
                {
                    "lat": 9.384333173382124,
                    "lng": 76.35669904868689
                },
                {
                    "lat": 9.419041877399508,
                    "lng": 76.35713367214326
                },
                {
                    "lat": 9.436976379090002,
                    "lng": 76.32862231615206
                },
                {
                    "lat": 9.420204940068771,
                    "lng": 76.29968959240415
                },
                {
                    "lat": 9.385508303082805,
                    "lng": 76.29926170184467
                },
                {
                    "lat": 9.367571037751722,
                    "lng": 76.3277598042203
                }
            ],
            "center_point": {
                "longitude": 76.32819435590856,
                "latitude": 9.402272618462488
            },
            
        },
        {
            "id": 14,
            "name": "Vayalar",
            "boundary": [
                {
                    "lat": 9.69674468605489,
                    "lng": 76.36061425029116
                },
                {
                    "lat": 9.73146130236402,
                    "lng": 76.36104977188604
                },
                {
                    "lat": 9.749345379603014,
                    "lng": 76.33250851868087
                },
                {
                    "lat": 9.732515719417012,
                    "lng": 76.30354502529723
                },
                {
                    "lat": 9.697811178285521,
                    "lng": 76.30311625076136
                },
                {
                    "lat": 9.679924221832591,
                    "lng": 76.33164422464004
                }
            ],
            "center_point": {
                "longitude": 76.33207967359279,
                "latitude": 9.714633747926174
            },
        },
        {
            "id": 15,
            "name": "Arthunkal",
            "boundary": [
                {
                    "lat": 9.64521481466633,
                    "lng": 76.33121222632435
                },
                {
                    "lat": 9.679924221832591,
                    "lng": 76.33164422464004
                },
                {
                    "lat": 9.697811178285521,
                    "lng": 76.30311625076136
                },
                {
                    "lat": 9.68099159646263,
                    "lng": 76.27416956345057
                },
                {
                    "lat": 9.64629427664192,
                    "lng": 76.27374430563204
                },
                {
                    "lat": 9.62840445097731,
                    "lng": 76.3022589967197
                }
            ],
            "center_point": {
                "longitude": 76.30269092792135,
                "latitude": 9.663106756477717
            },
        },
        {
            "id": 16,
            "name": "Cherthala town",
            "boundary": [
                {
                    "lat": 9.644125065271501,
                    "lng": 76.38872005087325
                },
                {
                    "lat": 9.67884653300728,
                    "lng": 76.38915879807585
                },
                {
                    "lat": 9.69674468605489,
                    "lng": 76.36061425029116
                },
                {
                    "lat": 9.679924221832591,
                    "lng": 76.33164422464004
                },
                {
                    "lat": 9.64521481466633,
                    "lng": 76.33121222632435
                },
                {
                    "lat": 9.627313810812973,
                    "lng": 76.35974350685822
                }
            ],
            "center_point": {
                "longitude": 76.36018217617715,
                "latitude": 9.662028188607595
            },
        }
    ],
    "number_of_zones": 10
}

# Define the projection systems
h3_projection = Proj(proj='latlong', datum='WGS84')
osm_projection = Proj(proj='latlong', datum='WGS84')

# Create a Folium map centered around the first zone
map_center = [zone_data["zones"][0]["boundary"][0]["lat"], zone_data["zones"][0]["boundary"][0]["lng"]]
mymap = folium.Map(location=map_center, zoom_start=12)

# Project and add zone boundaries to the map
for zone in zone_data["zones"]:
    boundary_coords = [(point["lat"], point["lng"]) for point in zone["boundary"]]
    osm_boundary_coords = [transform(h3_projection, osm_projection, lat, lng) for lat, lng in boundary_coords]
    polygon = Polygon(osm_boundary_coords)

    folium.Polygon(
        locations=polygon.exterior.coords[:],
        popup=zone["name"],
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.3,
    ).add_to(mymap)





# Save the map to an HTML file
mymap.save('index.html')
