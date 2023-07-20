def test_home(client):
    landing = client.get("/")
    html = landing.data.decode()
    assert "<title>Flask Blog</title>" in html

    assert '<a class="nav-item nav-link" href="/home">Home</a>' in html
    assert '<a class="nav-item nav-link" href="/about">About</a>' in html
    assert '<a class="nav-item nav-link" href="/login">Login</a>' in html
    assert '<a class="nav-item nav-link" href="/register">Register</a>' in html



    assert landing.status_code == 200

def test_home_aliases(client):
    landing = client.get("/")
    assert client.get("/home").data == landing.data


def test_about(client):
    landing = client.get("/about")
    html = landing.data.decode()
    assert "<title>Flask Blog - About</title>" in html
