# AutoDownloadReferences
Automatically download PDFs of a paper's references

Currently only working with DOI papers available at ACM Digital Library.
All PDFs are retrieved from Google Scholar, therefore they all have free access granted, i.e., there's no piracy involved in this crawling.

## Setup

```
pip3 install selenium==3.11.0
```
Also download ```chromedriver``` for your system [from here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Usage

```
usage: getreferences.py [-h] doi

Get all the PDFs in a paper's reference

positional arguments:
  doi         tries to find and download all paper's references

optional arguments:
  -h, --help  show this help message and exit
```

## Example

```
python3 getreferences.py 10.1145/3145749.3149444

1 of 19: http://papers.nips.cc/paper/3151-an-application-of-reinforcement-learning-to-aerobatic-helicopter-flight.pdf
2 of 19: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.60.8161&rep=rep1&type=pdf
3 of 19: Could not find the pdf for: D.H. Choi, I.H. Jang, M.H. Kim, and N.C. Kim. 2007. Color Image Enhancement Based on Single-Scale Retinex with a JND-based Nonlinear Filter. In ISCAS. 3948âĂŞ3951. 	 Skipping...
4 of 19: Could not find the pdf for: Kaiming He , Jian Sun , Xiaoou Tang, Guided Image Filtering, IEEE Transactions on Pattern Analysis and Machine Intelligence, v.35 n.6, p.1397-1409, June 2013  [doi>10.1109/TPAMI.2012.213] 	 Skipping...
5 of 19: Could not find the pdf for: T.-H. Huang, C.-K. Liang, S.-L. Yeh, and H.-H. Chen. 2008. JND-Based Enhancement of Perceptibility for Dim Images. In IEEE ICIP. 1752--1755. 	 Skipping...
6 of 19: https://pdfs.semanticscholar.org/30b6/314646f18a17d2c811aa17b18ed69160d6a6.pdf
7 of 19: https://arxiv.org/pdf/0710.4710.pdf
8 of 19: http://www.mpedram.com/Papers/HVS-aware-DBS-journal.pdf
9 of 19: http://repository.cmu.edu/cgi/viewcontent.cgi?article=2134&context=robotics.pdf
10 of 19: Could not find the pdf for: Chulwoo Lee , Chul Lee , Young-Yoon Lee , Chang-Su Kim, Power-Constrained Contrast Enhancement for Emissive Displays Based on Histogram Equalization, IEEE Transactions on Image Processing, v.21 n.1, p.80-93, January 2012  [doi>10.1109/TIP.2011.2159387]  Skipping...
11 of 19: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.707.615&rep=rep1&type=pdf
12 of 19: Could not find the pdf for: V. Mnih, K. Kavukcuoglu, D. Silver, A.A. Rusu, J. Veness, M.G. Bellemare, A. Graves, M. Riedmiller, A.K. Fidjeland, G. Ostrovski, S. Petersen, C. Beattie, A. Sadik, I. Antonoglou, H. King, D. Kumaran, D. Wierstra, S. Legg, and D. Hassabis. 2015. Human-level control through deep reinforcement learning. Nature Letter 518 (2015), 529--533. 	 Skipping...
13 of 19: Could not find the pdf for: S.-C. Pei, W.-W. Chang, and C.-T. Shen. 2014. Saliency Detection using Superpixel Belief Propagation. In IEEE ICIP. 1135--1139. 	 Skipping...
14 of 19: Could not find the pdf for: S.-C. Pei, C.-T. Shen, and T.-Y. Lee. 2012. Visual Enhancement using Constrained L0 Gradient Image Decomposition for Low Backlight Displays. IEEE SPL 19(12) (2012), 813--816. 	 Skipping...
15 of 19: Could not find the pdf for: C.-T. Shen, Z. Lu, Y.-P. Hung, and S.-C. Pei. 2016. Visual Enhancement Using Sparsity-Based Image Decomposition for Low Backlight Displays. In IEEE ISCAS. 2563--2566. 	 Skipping...
16 of 19: https://www.researchgate.net/profile/Homer_Chen/publication/284781258_Exploiting_Perceptual_Anchoring_for_Color_Image_Enhancement/links/5772788308aeeec38953e3c8.pdf
17 of 19: https://pdfs.semanticscholar.org/1740/eb993cc8ca81f1e46ddaadce1f917e8000b5.pdf
18 of 19: https://pdfs.semanticscholar.org/2105/a10182adaf4f4f1e897f30ed5af0e1f11da0.pdf
19 of 19: https://pdfs.semanticscholar.org/a074/c93f8e74f8aff906bb1bea1c971fd737c4b3.pdf
1 of 11: Downloading http://papers.nips.cc/paper/3151-an-application-of-reinforcement-learning-to-aerobatic-helicopter-flight.pdf ...
2 of 11: Downloading http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.60.8161&rep=rep1&type=pdf ...
3 of 11: Downloading https://pdfs.semanticscholar.org/30b6/314646f18a17d2c811aa17b18ed69160d6a6.pdf ...
4 of 11: Downloading https://arxiv.org/pdf/0710.4710.pdf ...
5 of 11: Downloading http://www.mpedram.com/Papers/HVS-aware-DBS-journal.pdf ...
6 of 11: Could not download http://repository.cmu.edu/cgi/viewcontent.cgi?article=2134&context=robotics.pdf
7 of 11: Could not download http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.707.615&rep=rep1&type=pdf
8 of 11: Downloading https://www.researchgate.net/profile/Homer_Chen/publication/284781258_Exploiting_Perceptual_Anchoring_for_Color_Image_Enhancement/links/5772788308aeeec38953e3c8.pdf ...
9 of 11: Downloading https://pdfs.semanticscholar.org/1740/eb993cc8ca81f1e46ddaadce1f917e8000b5.pdf ...
10 of 11: Downloading https://pdfs.semanticscholar.org/2105/a10182adaf4f4f1e897f30ed5af0e1f11da0.pdf ...
11 of 11: Downloading https://pdfs.semanticscholar.org/a074/c93f8e74f8aff906bb1bea1c971fd737c4b3.pdf ...
```
