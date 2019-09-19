# import datetime
# from haystack import indexes
# from Analytics.models import busarrivalv2
#
# class busarrivalv2Index(indexes.SearchIndex, indexes.Indexable):
#     service_number = indexes.CharField(max_length=6,null=True,blank=True)
#     operator = indexes.CharField(max_length=6,null=True,blank=True)
#     destination_code = indexes.CharField(max_length=50,null=True,blank=True)
#     estimated_arrival = indexes.CharField(max_length=220,null=True,blank=True)
#     feature =  indexes.CharField(max_length=10,null=True,blank=True)
#     latitude = indexes.CharField(max_length=100,null=True,blank=True)
#     longitute = indexes.CharField(max_length=100,null=True,blank=True)
#     load = indexes.CharField(max_length=10,null=True,blank=True)
#     origin_code = indexes.CharField(max_length=20,null=True,blank=True)
#     type = indexes.CharField(max_length=5,null=True,blank=True)
#     visit_number = indexes.CharField(max_length=3,null=True,blank=True)
#     last_updated_time = indexes.DateTimeField(auto_now=True,blank=True,null=True)
#
#     def get_model(self):
#         return busarrivalv2
#
#     def index_queryset(self, using=None):
#         """Used when the entire index for model is updated."""
#         return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
#
