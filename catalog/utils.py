from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from catalog.models import Products


def q_search(query):


    # return Products.objects.annotate(search=SearchVector("name", "description")).filter(search=query)

    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    return Products.objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")


    # keywords = [word for word in query.split() if len(word) > 2]

    # q_objects = Q()

    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)



    # return Products.objects.filter(q_objects)