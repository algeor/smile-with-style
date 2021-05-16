import requests as r

def extract_from_url():
    url = 'https://raw.githubusercontent.com/enthought/Numpy-Tutorial-SciPyConf-2019/master/exercises/wind_statistics/wind.data'
    req = r.get(url, allow_redirects=True)

    with open("wind.data", "wb") as file:
        file.write(req.content)
    return print('File with data created!')
