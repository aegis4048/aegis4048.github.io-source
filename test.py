import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

def generate_collinear_data(cov, size=50, coefs=[0, 0], intercept=0, means=[0, 0, 0], loc=0, scale=1):

    # random generation of 3D gaussian collinear features.
    X = np.random.multivariate_normal(mean=means, cov=cov, size=size)

    print(size)

    # generate gaussian white noise.
    gaussian_noise = np.random.normal(loc=loc, scale=scale, size=size)

    # make the outcome.
    y = intercept + coefs[0] * X[:, 0] + coefs[1] * X[:, 1] + gaussian_noise

    # train
    ols = linear_model.LinearRegression()
    model = ols.fit(X, y)

    return model.coef_, model.intercept_

# settings
m = 2000                               # number of simulations
n = 100                               # sample size
true_coefs = [13, 0.5]                   # linear regression coefficients, 3 features
true_intercept = 2                    # y-intercept
feature_means = [5, 1]            # means of gaussian features. This is not important
correlation_lo = 0.01                 # degree of collinearity (LOW)
correlation_hi = 0.95                 # degree of collinearity (HIGH)

# high collinearity covariance matrix
cov_hi = np.full((len(true_coefs), len(true_coefs)), correlation_hi)
np.fill_diagonal(cov_hi, 1)

# low collinearity covariance matrix
cov_lo = np.full((len(true_coefs), len(true_coefs)), correlation_lo)
np.fill_diagonal(cov_lo, 1)

# simulation
model_hi_col_coefs = []
model_lo_col_coefs = []
for i in range(m):
    model_hi_col_coefs.append(
        generate_collinear_data(cov_hi, size=n, coefs=true_coefs, intercept=true_intercept, means=feature_means, loc=0, scale=2)[0]
    )
    model_lo_col_coefs.append(
        generate_collinear_data(cov_lo, size=n, coefs=true_coefs, intercept=true_intercept, means=feature_means, loc=0, scale=2)[0]
    )

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
plt.show()