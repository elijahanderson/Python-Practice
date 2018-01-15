import tensorflow as tf

# When using Jupyter notebook make sure to call tf.reset_default_graph() at the beginning to clear the symbolic graph
# before defining new nodes.
tf.reset_default_graph()

x = tf.random_normal([10, 10])
y = tf.random_normal([10, 10])
z = tf.matmul(x, y)

"""
    Operations in tensorflow are symbolic, so we need to create a Session object and run it to perform the calculation.

    If we try printing z_val directly we get:
        Tensor("MatMul:0", shape=(10, 10), dtype=float32)
    
"""
sess = tf.Session()
z_val = sess.run(z)

print(z_val)

"""
To understand how powerful symbolic computation can be let's have a look at another example. Assume that we have samples
 from a curve (say f(x) = 5x^2 + 3) and we want to estimate f(x) based on these samples. We define a parametric function
  g(x, w) = w0 x^2 + w1 x + w2, which is a function of the input x and latent parameters w, our goal is then to find the
   latent parameters such that g(x, w) ≈ f(x). This can be done by minimizing the following loss function: 
   L(w) = ∑ (f(x) - g(x, w))^2. Although there's a closed form solution for this simple problem, we opt to use a more 
   general approach that can be applied to any arbitrary differentiable function, and that is using stochastic gradient 
   descent. We simply compute the average gradient of L(w) with respect to w over a set of sample points and move in 
   the opposite direction.

Here's how it can be done in TensorFlow:
"""
import numpy as np

# Placeholders are used to feed values from python to TensorFlow ops. We define
# two placeholders, one for input feature x, and one for output y.
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# Assuming we know that the desired function is a polynomial of 2nd degree, we
# allocate a vector of size 3 to hold the coefficients. The variable will be
# automatically initialized with random noise.
w = tf.get_variable("w", shape=[3, 1])

# We define yhat to be our estimate of y.
# tf.stack() packs the argument tensors into one tensor
# tf.ones_like creates a tensor of ones in the same shape as the argument tensor
f = tf.stack([tf.square(x), x, tf.ones_like(x)], 1)
# tf.squeeze() returns the same tensor but with all dimensions of size 1 removed
yhat = tf.squeeze(tf.matmul(f, w), 1)

# The loss is defined to be the l2 distance between our estimate of y and its
# true value. We also added a shrinkage term, to ensure the resulting weights
# would be small.

# loss measures error between two tensors, or between a tensor and zero. It basically
# measures the accuracy of a network in a regression task
loss = tf.nn.l2_loss(yhat - y) + 0.1 * tf.nn.l2_loss(w)

# We use the Adam optimizer with learning rate set to 0.1 to minimize the loss.
train_op = tf.train.AdamOptimizer(0.1).minimize(loss)

def generate_data():
    x_val = np.random.uniform(-10.0, 10.0, size=100)
    y_val = 5 * np.square(x_val) + 3
    return x_val, y_val

sess = tf.Session()

# Since we are using variables we first need to initialize them.
sess.run(tf.global_variables_initializer())
for _ in range(1000):
    x_val, y_val = generate_data()
    _, loss_val = sess.run([train_op, loss], {x: x_val, y: y_val})
    print(loss_val)

print(sess.run([w]))