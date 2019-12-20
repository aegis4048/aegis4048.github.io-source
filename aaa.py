import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

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
m = 2000                                 # number of simulations
correlation_lo = 0.01                    # degree of collinearity (LOW)
correlation_hi = 0.98                    # degree of collinearity (HIGH)

kwargs = {
    'n': 100,                            # sample size
    'true_coefs': [13, 0.5],             # linear regression coefficients, 2 features
    'true_intercept': 2,                 # y-intercept
    'feature_means': [0, 0],             # means multivariate normal distribution. This is not important
    'loc': 0,                            # mean of gaussian noise
    'scale': 1                           # standard deviation of gaussian noise
}

# high collinearity covariance matrix
cov_hi = np.full((len(kwargs['true_coefs']), len(kwargs['true_coefs'])), correlation_hi)
np.fill_diagonal(cov_hi, 1)

# low collinearity covariance matrix
cov_lo = np.full((len(kwargs['true_coefs']), len(kwargs['true_coefs'])), correlation_lo)
np.fill_diagonal(cov_lo, 1)

# simulation
model_hi_col_coefs = []
model_lo_col_coefs = []
for i in range(m):

    X_hi, y_hi = generate_collinear_data(cov_hi, **kwargs)
    ols_hi = linear_model.LinearRegression()
    model_hi = ols_hi.fit(X_hi, y_hi)
    model_hi_col_coefs.append(model_hi.coef_)

    X_lo, y_lo = generate_collinear_data(cov_lo, **kwargs)
    ols_lo = linear_model.LinearRegression()
    model_lo = ols_lo.fit(X_lo, y_lo)
    model_lo_col_coefs.append(model_lo.coef_)

# list to numpy array conversion
model_hi_col_coefs = np.array(model_hi_col_coefs)
model_lo_col_coefs = np.array(model_lo_col_coefs)

# plotting
plt.style.use('default')
plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(8, 4.5))

ax.scatter(model_hi_col_coefs[:, 0], model_hi_col_coefs[:, 1], s=10, label='High multicollinearity',
           edgecolor='red', facecolor='firebrick', alpha=0.7)
ax.scatter(model_lo_col_coefs[:, 0], model_lo_col_coefs[:, 1], s=10, label='Low multicollinearity',
           edgecolor='dimgrey', facecolor='k', alpha=0.7)

ax.set_xlim(10.5, 15.5)
ax.set_ylim(-2, 3)
ax.set_xlabel('$x_1$ coefficient values', fontsize=16)
ax.set_ylabel('$x_2$ coefficient values', fontsize=16)
ax.set_title('Model instability due to multicollinearity', fontsize=20)
ax.legend(facecolor='white', fontsize=11)
ax.text(0.2, 0.1, 'aegis4048.github.io', fontsize=13, ha='center', va='center',
         transform=ax.transAxes, color='grey', alpha=0.5)

fig.tight_layout()