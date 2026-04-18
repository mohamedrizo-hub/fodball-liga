from django.db import models
class League(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    season = models.CharField(max_length=20)
    founded_year = models.IntegerField()
    logo = models.ImageField(upload_to='league_logos/')
    president = models.CharField(max_length=100)
    website = models.URLField()
    sponsor = models.CharField(max_length=100)
    total_teams = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    founded_year = models.IntegerField()
    stadium = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/')
    budget = models.FloatField()
    website = models.URLField()
    owner = models.CharField(max_length=100)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=10)
    number = models.IntegerField()
    nationality = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    salary = models.FloatField()
    join_date = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away')
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    date = models.DateTimeField()
    stadium = models.CharField(max_length=100)
    referee = models.CharField(max_length=100)
    attendance = models.IntegerField()
    weather = models.CharField(max_length=50)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"

class Statistic(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    goals = models.IntegerField()
    assists = models.IntegerField()
    matches_played = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    shots = models.IntegerField()
    passes = models.IntegerField()
    tackles = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return str(self.player)

class Coach(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)
    experience_years = models.IntegerField()
    salary = models.FloatField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    trophies = models.IntegerField()
    contract_start = models.DateField()
    contract_end = models.DateField()
    license_level = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Stadium(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    capacity = models.IntegerField()
    built_year = models.IntegerField()
    owner = models.CharField(max_length=100)
    surface = models.CharField(max_length=50)
    cost = models.FloatField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='stadiums/')

    def __str__(self):
        return self.name

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    from_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='from_team')
    to_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='to_team')
    transfer_fee = models.FloatField()
    date = models.DateField()
    contract_years = models.IntegerField()
    agent = models.CharField(max_length=100)
    salary = models.FloatField()
    bonus = models.FloatField()
    transfer_type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.player)

class Referee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)
    experience = models.IntegerField()
    matches_officiated = models.IntegerField()
    yellow_cards_given = models.IntegerField()
    red_cards_given = models.IntegerField()
    rating = models.FloatField()
    salary = models.FloatField()
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    budget = models.FloatField()
    contract_start = models.DateField()
    contract_end = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='sponsors/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name
class Training(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.IntegerField()
    location = models.CharField(max_length=100)
    focus_area = models.CharField(max_length=100)
    intensity = models.CharField(max_length=50)
    attendance = models.IntegerField()
    notes = models.TextField()
    weather = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.team} training"

class Injury(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    injury_type = models.CharField(max_length=100)
    severity = models.CharField(max_length=50)
    date_injured = models.DateField()
    expected_return = models.DateField()
    doctor = models.CharField(max_length=100)
    treatment = models.TextField()
    matches_missed = models.IntegerField()
    recovery_status = models.CharField(max_length=50)
    notes = models.TextField()

    def __str__(self):
        return f"{self.player} injury"

class Ticket(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=20)
    price = models.FloatField()
    buyer_name = models.CharField(max_length=100)
    buyer_email = models.EmailField()
    purchase_date = models.DateTimeField()
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    gate = models.CharField(max_length=10)
    section = models.CharField(max_length=50)

    def __str__(self):
        return f"Ticket {self.seat_number}"
