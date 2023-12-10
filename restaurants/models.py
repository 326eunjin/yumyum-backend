from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.db import models


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    operating_hour = models.JSONField()
    name = models.CharField(max_length=30)
    category = ArrayField(models.IntegerField())
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    location = models.GeometryField(srid=4326)
    address = models.CharField()

    queue = models.ManyToManyField(
        "Reservation",
        through="ReservationQueue",
        related_name="restaurant_set",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = "Restaurant"
    
    def calculate_star_avg(self):
        # 해당 레스토랑의 리뷰를 기반으로 평균 별점을 계산
        avg_rating = self.review_set.aggregate(models.Avg('stars'))['stars__avg']
        return avg_rating if avg_rating is not None else 0


# Restaurant - User 관계의 중간테이블
class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, null=True, blank=True
    )
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    reservation_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["reservation_id"]


# Restaurant - Reservation 관계의 중간테이블
class ReservationQueue(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        unique_together = ("reservation", "restaurant")


class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = "Manager"


# class OperatingHours(models.Model):
#     operating_hours_id = models.AutoField(primary_key=True)
#     restaurant = models.OneToOneField(Restaurant, related_name='_operating_hours', on_delete=models.CASCADE)
#     day_of_week = models.IntegerField(blank=True, null=True)
#     start_time = models.DateTimeField(blank=True, null=True)
#     end_time = models.DateTimeField(blank=True, null=True)
#     etc_reason = models.TextField(blank=True, null=True)  # This field type is a guess.
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         managed = False
#         db_table = "Operating_hours"
