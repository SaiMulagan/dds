// Raw data query
db.yelp_business_raw.find(
  { state: "CA", stars: { $gte: 4 } }
).limit(5)

// Aggregated city stats
db.yelp_city_stats.find(
  { business_count: { $gt: 100 } }
)

// Aggregated category stats
db.yelp_category_stats.find(
  { avg_stars: { $gte: 4.0 } }
).sort({ business_count: -1 })