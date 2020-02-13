import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def generate_collinear_data(cov, n=10, true_coefs=[0, 0], true_intercept=0, feature_means=[0, 0, 0], loc=0, scale=1):
    # random generation of 3D gaussian collinear features.
    X = np.random.multivariate_normal(mean=feature_means, cov=cov, size=n)

    # generate gaussian white noise.
    gaussian_noise = np.random.normal(loc=loc, scale=scale, size=n)

    # make the outcome.
    y = true_intercept + gaussian_noise
    for i in range(len(true_coefs)):
        y += true_coefs[i] * X[:, i]

    return X, y


# settings
m = 10000  # number of simulations
correlation = 0.98  # degree of collinearity (HIGH)

kwargs = {
    'n': 1000,  # sample size
    'true_coefs': [13, 0.5, 5],  # linear regression coefficients, 2 features
    'true_intercept': 2,  # y-intercept
    'feature_means': [-12, 14, 2],  # means multivariate normal distribution. This is not important
    'loc': 0,  # mean of gaussian noise
    'scale': 1  # standard deviation of gaussian noise
}

# high collinearity covariance matrix
cov = np.full((len(kwargs['true_coefs']), len(kwargs['true_coefs'])), correlation)
np.fill_diagonal(cov, 1)

# simulation
size_hi_params = []
size_lo_params = []
for i in range(m):
    # high collinearity data
    X_hi, y_hi = generate_collinear_data(cov, **kwargs)
    interaction_hi_1 = X_hi[:, 0].reshape(-1, 1) ** 2  # x1^2
    interaction_hi_2 = X_hi[:, 1].reshape(-1, 1) * X_hi[:, 2].reshape(-1, 1)  # x2 * x3
    X_hi = np.concatenate([X_hi, interaction_hi_1, interaction_hi_2], axis=1)
    X_st_hi = sm.add_constant(X_hi)
    model_hi = sm.OLS(y_hi, X_st_hi).fit()
    size_hi_params.append(model_hi.params)

    # low collinearity data
    X_lo, y_lo = generate_collinear_data(cov, **kwargs)
    interaction_lo_1 = X_lo[:, 0].reshape(-1, 1) ** 2
    interaction_lo_2 = X_lo[:, 1].reshape(-1, 1) * X_lo[:, 2].reshape(-1, 1)
    X_lo = np.concatenate([X_lo, interaction_lo_1, interaction_lo_2], axis=1)
    scaler = StandardScaler(with_std=False)
    X_lo, y_lo = scaler.fit_transform(X_lo), scaler.fit_transform(y_lo.reshape(-1, 1)).flatten()
    X_st_lo = sm.add_constant(X_lo)
    model_lo = sm.OLS(y_lo, X_st_lo).fit()
    size_lo_params.append(model_lo.params)

# list to numpy conversion
size_hi_params = np.asarray(size_hi_params)
size_lo_params = np.asarray(size_lo_params)


# plotting
def styling(ax):
    ax.set_facecolor('#eeeeee')
    ax.grid(True, linestyle='--', color='#acacac')
    ax.tick_params(color='grey')
    _ = [spine.set_edgecolor('grey') for spine in ax.spines.values()]
    ax.text(0.5, 0.1, 'aegis4048.github.io', fontsize=12, ha='center', va='center',
            transform=ax.transAxes, color='grey', alpha=0.5)


boxplot_styling = {
    'sym': '',
    'whis': [2.5, 97.5],
    'showfliers': False,
    'boxprops': dict(linewidth=2.0, color='#4e98c3'),
    'whiskerprops': dict(linewidth=2.0, color='#4e98c3', linestyle='--'),
    'vert': True,
    'capprops': dict(linewidth=2.0, color='k'),
    'medianprops': dict(linewidth=2.0, color='#ad203e'),
    'widths': (0.4, 0.4)
}

labels = ['Intercept', '$X_1$', '$X_2$', '$X_3$', '$X_1^2$', '$X_2X_3$']

fig, axes = plt.subplots(1, len(labels), figsize=(16, 6))

for i, (ax, label) in enumerate(zip(axes, labels)):
    ax.boxplot([list(size_hi_params[:, i]), list(size_lo_params[:, i])], **boxplot_styling)
    styling(ax)
    ax.set_title(label, fontsize=20, y=-0.2)
    ax.set_xticklabels(['n = %.d' % 1, 'n = %.d' % 2], fontsize=15)

fig.tight_layout(rect=[0, 0.05, 1, 0.91])
fig.suptitle('Range of coefficients with big & small sample sizes - %.f simulations' % m, fontsize=25);