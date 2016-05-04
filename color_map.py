import csv
import webbrowser
from BeautifulSoup import BeautifulSoup

def color_mapper(value):
    '''
    Map a value between 0 and 1 to rgb value. 0 is blue, 1 is red
    Returns a tuple of rgb value
    '''
    if value < 0.2:
        value = 0.2
    elif value > 0.8:
        value = 0.8 
    #remapping value to rgb range
    value -= 0.2
    value = value/0.6
    
    red = int(value*255)
    blue = int(255-value*255)
    return (red, 0 ,blue)

def map_states(w_value,s_value,ne_value,mw_value,search_query):
    '''
        Given average sentiment value of each region, saves a choropleth map representing different sentiment value in different US region.
    '''
    svg = open('Blank_US_Map.svg','r').read()
    soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview','path'])

    new_map = open('choropleth_map.svg','w') 

    #Finding text tag that will display a topic keyword
    # soup.find(text="US Map").replaceWith(search_query)
    # text = soup.style
    # soup.find('text')['x'] = 480 - (len(search_query)/2 * 35)
   
    # #Display sentiment value
    # soup.find(text="Northeastern Value").replaceWith("NE: {0:.5f}".format(ne_value))
    # soup.find(text="West Value").replaceWith("W: {0:.5f}".format(w_value))
    # soup.find(text="Midwest Value").replaceWith("MW: {0:.5f}".format(mw_value))
    # soup.find(text="South Value").replaceWith("S: {0:.5f}".format(s_value))
 
    #Find states
    paths = soup.findAll('path')

    path_style = '''font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;
    marker-start:none;stroke-linejoin:bevel;fill:'''

    #states categorization
    west = ["MT","WY","CO","NM","ID","UT","AZ","NV","WA","OR","CA"]
    south = ['FL','GA','NC','SC','VA','WV','DE','AL','KY','MS','TN','AR','LA','OK','TX']
    northeast = ['MD','CT','DE','ME','MA','NH','NJ','NY','PA','RI','VT']
    midwest = ['ND','SD','NE','KS','MN','IA','MO','WI','IL','MI','IN','OH']

    for p in paths:
        try:
            if p['id'] in west:
                color = 'rgb' + str(color_mapper(w_value))
                p['style'] = path_style + color
            if p['id'] in south:
                color = 'rgb' + str(color_mapper(s_value))
                p['style'] = path_style + color
            if p['id'] in northeast:
                color = 'rgb' + str(color_mapper(ne_value))
                p['style'] = path_style + color
            if p['id'] in midwest:
                color = 'rgb' + str(color_mapper(mw_value))
                p['style'] = path_style + color
        except:
            continue 

    new_map.write(soup.prettify())
    new_map.close()
    #webbrowser.open('choropleth_map.svg')
