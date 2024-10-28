from ScreenRecorder import *
from generateFrames import *
from generateEmbeddings import *
from query_embedding import *

# RecordVideo()
temp=FolderSize()
str=f"output_{temp}.avi"
# generate_frames(str)
embeddings=generate_embeddings(str)
query_embeddings_faiss(embeddings)