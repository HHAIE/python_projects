from lastEps import down_last_eps
from epsAn4up import down_eps_an4up
from epsGogo import down_eps_gogo

# Check a list of animes for new episodes and download them if found
followed_animes = ["One Piece", "Chainsaw Man", "Mairimashita! Iruma-kun 3rd Season", "Spy x Family Part 2", "Shinobi no Ittoki", "Xian Wang de Richang Shenghuo 3", "Mob Psycho 100 III", "Bleach: Sennen Kessen-hen", "Boku no Hero Academia 6th Season", "Yowamushi Pedal: Limit Break", "Detective Conan"]
down_last_eps(followed_animes)


# Url and name of an anime and number of wanted episodes to download from anime4up
url = "https://anime4up.tv/anime/one-piece/"
name = "One Piece"
eps_count = 10

down_eps_an4up(url, name, eps_count)


# Url and name of an anime and number of wanted episodes to download from gogoanime
url = "https://gogoanime.run/category/one-piece"
name = "One Piece"
eps_count = 10

down_eps_gogo(url, name, eps_count)