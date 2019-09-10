def generate_time_series(k=200, m=1000, noise_mean=0, noise_std=100, n=50, start_date=datetime.date(2017, 7, 1)):
    """
    :param k: slope, increment in upwards/downwards trend (step size)
    :param m: y-intercept
    :param noise_mean: mean, parameter for generating random gaussian noise
    :param noise_std: standard deviation, parameter for generating random gaussian noise
    :param n: number of samples
    :param start_date: start point in time-series
    :return:
    """
    xs = np.linspace(0, 1, n, endpoint=False)
    gaussian_noise = random.gauss(noise_mean, noise_std)
    ys = [k * x + m + gaussian_noise for x in xs]
    ts = [start_date + datetime.timedelta(x) * 365 for x in xs]
    return xs, ys, ts


xs, ys, ts = generate_time_series()




