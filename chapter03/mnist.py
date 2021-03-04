import urllib.request
import os
import os.path
import gzip
import pickle
import numpy as np

url_base = 'http://yann.lecun.com/exdb/mnist/'
key_file = {
    'train_img': 'train-images-idx3-ubyte.gz',
    'train_label': 'train-labels-idx1-ubyte.gz',
    'test_img': 't10k-images-idx3-ubyte.gz',
    'test_label': 't10k-labels-idx1-ubyte.gz'
}

dataset_dir = os.path.dirname(os.path.abspath(__file__))
save_file = dataset_dir + "mnist.pkl"

train_num = 60000
test_num = 10000
img_dim = (1, 28, 28)
img_size = 784


def _set_header_for(url, file_path):
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent',
                     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36')
    opener.retrieve(url, file_path)


def _download(file_name):
    file_path = dataset_dir + "/" + file_name

    if os.path.exists(file_path):  # ファイルが既に存在していれば終了
        return

    print(f"Downloading {file_name} ...")
    _set_header_for(url_base + file_name, file_path)
    print("Done")


def download_mnist():
    for v in key_file.values():
        _download(v)


def _load_label(file_name):
    file_path = dataset_dir + "/" + file_name

    print(f"Converting {file_name} to NumPy Array ...")
    with gzip.open(file_path, 'rb') as f:
        labels = np.frombuffer(f.read(), dtype=np.uint8, offset=8)
    print("Done")

    return labels


def _load_img(file_name):
    file_path = dataset_dir + "/" + file_name

    print(f"Converting {file_name} to NumPy Array ...")
    with gzip.open(file_path, 'rb') as f:
        data = np.frombuffer(f.read(), dtype=np.uint8, offset=16)
        print(data.shape)
    data = data.reshape(-1, img_size)
    print("Done")

    return data


def _convert_numpy():
    dataset = {}
    dataset['train_img'] = _load_img(key_file['train_img'])
    dataset['train_label'] = _load_label(key_file['train_label'])
    dataset['test_img'] = _load_img(key_file['test_img'])
    dataset['test_label'] = _load_label(key_file['test_label'])

    return dataset


def init_mnist():
    download_mnist()
    dataset = _convert_numpy()
    print("Creating pickle file ...")
    with open(save_file, 'wb') as f:
        pickle.dump(dataset, f, -1)
    print("Done")


def _change_one_hot_label(X):
    T = np.zeros((X.size, 10))
    for idx, row in enumerate(T):
        row[X[idx]] = 1

    return T


def load_mnist(normalize=True, flatten=True, one_hot_label=False):
    """
    MNIST データセットの読み込み

    Args:
        normalize: 画像のピクセル値を [0.0 - 1.0] に正規化する
        flatten: 画像を一次元配列にする
        one_hot_label: ラベルを one-hot 配列として返す

    Return:
        (訓練画像, 訓練ラベル), (テスト画像, テストラベル)

    Note:
        one-hot 配列とは [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] のような配列
    """
    if not os.path.exists(save_file):
        init_mnist()

    with open(save_file, 'rb') as f:
        dataset = pickle.load(f)

    if normalize:
        for key in ('train_img', 'test_img'):
            dataset[key] = dataset[key].astype(np.float32)
            dataset[key] /= 255.0

    if one_hot_label:
        for key in ('train_label', 'test_label'):
            dataset[key] = _change_one_hot_label(dataset[key])

    if not flatten:
        for key in ('train_img', 'test_img'):
            dataset[key] = dataset[key].reshape(-1, 1, 28, 28)

    return (dataset['train_img'], dataset['train_label']), (dataset['test_img'], dataset['test_label'])
