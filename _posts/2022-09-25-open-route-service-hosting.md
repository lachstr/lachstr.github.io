---
layout: post
title: "Hosted Open Route Service"
categories: engineering
---

[Open Route Service](https://openrouteservice.org/) (ORS) is an open source API that can be used to find public-road routes between GPS coordinates. We intended to use ORS to perform feature engineering on a dataset. This post documents our experience using ORS as a server and client.

## Techincal Background

ORS is a containerised Java Spring Boot application, running Apache Tomcat webserver. It uses Dijkstra's algorithm to compute graphs on startup and uses this data to efficiently provide the shortest route between GPS coordinates.

The ORS team kindly provides a free API as a public service. Unfortunately for us, this is limited to 2000 requests per day. We required around 100,000 requests to complete the processing on our dataset, this equates to around 50 days of processing. Fortunately, being open source, it is possible to host your own ORS instance for these purposes. This post will document our experience doing so. Spoiler alert: we were able to go from 1.4 requests per minute to 30,000 requests per minute (~21,000x increase).

## Server Configuration

We used the guide here: [Open Route Service - Docker](https://giscience.github.io/openrouteservice/installation/Running-with-Docker.html)

We suggest looking at the YouTube link on that page, as we didn't find the guide to be clear on exactly what was and wasn't required.

We created a Google Cloud instance for our server, and would reccommend doing so over hosting it locally.

We noted that:

- The developers say the minimum RAM required is 2 times the map size
    - We used the Australia map (500MB) and the JVM crashed due to insufficient memory when given 4 GB of RAM, the JVM appears to run steadily with 6GB of RAM (we allowed it to use upto 12GB)

- We didn't see any requirements on the minimum amount of storage
    - The JVM crashed due to insufficeint storage when allocated the Google Cloud default of 10GB, our instance uses around 11 GB

Its important to note that you won't be alerted of these errors until the graph building process is interrupted, which can take a few hours to do. Once crashed, you will need to build the graphs from scratch again, so its worth being liberal here to avoid fustrations.

We ended up using the following instance:
- Machine: n2d-standard-4 (4 vCPU + 16 GB memory)
- Storage: 20 GB boot disk
- Cost: $112.25/month (about $0.15/hour)


## Client Side

Initialy we used the Python `requests` library for our client. We were able to increase our throughput from 1.4 per minute to 500 per minute, that meant we could process the entire dataset in just... 3.5 hours! Thats a sure improvement over 50 days. However, it was noted that CPU utilisation on the server never surpasssed a few percent.

This made me wonder what was bottlenecking the performance. I suspected it was the series nature of the requests. Using the `requests` library, we were waiting for the first request to be served successfully before sending the second request and so on. This meant 99% of the instance's processing power was never being utlisied!

If instead, we could send the requests in parallel (without waiting for their responses before sending the subsequent ones) how much better could we do?

Fortunately, this problem has been addressed before and we found the [`grequests` library]() would do the trick. By paralellising the requests we were able to process at 30,000 requests per minute. This means our entire dataset could be processed in just over 3 minutes!

The following video shows a batch of our requests being processed.

<video width="680" height="382" controls>
	<source src="{{ site.baseurl }}/assets/parallel-req.mp4" type="video/mp4">
</video>

This is one of the reasons I love computing, in many engineering fields performance improvments of fractions of a percent are noteworthy (mechanical, electrical etc) - in computing performance improvements of 21,000x are possible!