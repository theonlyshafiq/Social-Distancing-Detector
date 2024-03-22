import cv2
import argparse
from src.Detector import Detector
from src.utils import calculate_centroids
from scipy.spatial import distance as dist


# python main.py -i "town.mp4"
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", help="The path of the input video")

    args = parser.parse_args()

    video_path = args.input

    detector = Detector()
    cap = cv2.VideoCapture(video_path)
    out = cv2.VideoWriter("output_video.mp4", cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30, (1280, 720))

    while True:
        ret, frame = cap.read()
        results = detector.find_people(frame)
        # print(results)
        centroids = calculate_centroids(results)

        violate = []

        if len(results) >= 2:
            D = dist.cdist(centroids, centroids, metric="euclidean")
            for i in range(0, D.shape[0]):
                for j in range(i + 1, D.shape[1]):
                    if D[i, j] < 65:
                        violate.append(i)
                        violate.append(j)

        for i, bbox in enumerate(results):
            startX, startY, endX, endY = bbox
            (cX, cY) = centroids[i]
            color = (0, 255, 0)
            if i in violate:
                color = (0, 0, 255)

            cv2.rectangle(frame, (int(startX), int(startY)), (int(endX), int(endY)), color, 2)
            cv2.circle(frame, (int(cX), int(cY)), 5, color, 1)

        text = "Social Distancing Violations: {}".format(len(violate))
        cv2.putText(frame, text, (10, frame.shape[0] - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.85, (0, 0, 255), 2)

        # Display Frames
        cv2.imshow("Frame", frame)
        out.write(frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()