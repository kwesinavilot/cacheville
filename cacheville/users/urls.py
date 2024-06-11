from django.db import models
from django.utils import timezone

class Building(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    total_floors = models.IntegerField()

    def __str__(self):
        return self.name

class Floor(models.Model):
    building = models.ForeignKey(Building, related_name='floors', on_delete=models.CASCADE)
    floor_number = models.IntegerField()

    def __str__(self):
        return f"{self.building.name} - Floor {self.floor_number}"

class Apartment(models.Model):
    floor = models.ForeignKey(Floor, related_name='apartments', on_delete=models.CASCADE)
    apartment_number = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.floor.building.name} - Floor {self.floor.floor_number} - Apartment {self.apartment_number}"

class Room(models.Model):
    ROOM_TYPES = [
        ('Bedroom', 'Bedroom'),
        ('Bathroom', 'Bathroom'),
        ('Kitchen', 'Kitchen'),
        ('Porch', 'Porch'),
        ('Living Room', 'Living Room'),
        ('Visitors Toilet', 'Visitors Toilet'),
    ]
    
    apartment = models.ForeignKey(Apartment, related_name='rooms', on_delete=models.CASCADE)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)

    def __str__(self):
        return f"{self.apartment} - {self.room_type}"

class Tenant(models.Model):
    TENANT_TYPES = [
        ('Family', 'Family'),
        ('Individual', 'Individual'),
    ]
    
    name = models.CharField(max_length=255)
    tenant_type = models.CharField(max_length=50, choices=TENANT_TYPES)
    apartment = models.ForeignKey(Apartment, related_name='tenants', on_delete=models.CASCADE)
    rooms_occupied = models.ManyToManyField(Room)

    def __str__(self):
        return self.name

class Payment(models.Model):
    tenant = models.ForeignKey(Tenant, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.tenant.name} - {self.amount} on {self.date_paid.strftime('%Y-%m-%d')}"
