https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# example from the website
# https://python-visualization.github.io/folium/
%reset -f

import folium

m = folium.Map(
    location=[45.5236, -122.6750],
    zoom_start=14
)

folium.Circle(
    radius=100,
    location=[45.5244, -122.6699],
    popup='The Waterfront',
    color='crimson',
    fill=False,
).add_to(m)

folium.CircleMarker(
    location=[45.5215, -122.6261],
    radius=50,
    popup='Laurelhurst Park',
    color='#3186cc',
    fill=True,
    fill_color='#3186cc'
).add_to(m)

m.save("foliumTest.html", "w")
print("browse in the output file: foliumTest.html")
print("exit code 0")
