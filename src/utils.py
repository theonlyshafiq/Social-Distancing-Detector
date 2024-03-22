def calculate_centroids(boxes):
    centroids = []
    for x1, y1, x2, y2 in boxes:
        # Calculate centroid coordinates
        centroid_x = (x1 + x2) / 2
        centroid_y = (y1 + y2) / 2
        centroids.append((centroid_x, centroid_y))
    return centroids