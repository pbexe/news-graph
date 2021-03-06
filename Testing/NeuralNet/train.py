from prepare import create_training_data, lexicon
import tensorflow as tf
import numpy as np

train_x, train_y, test_x, test_y = create_training_data(lexicon())

n_nodes_hl1 = 1500
n_nodes_hl2 = 1500
n_nodes_hl3 = 1500

n_classes = 2
batch_size = 100
hm_epochs = 12

x = tf.placeholder('float')
y = tf.placeholder('float')


# Nothing changes
def model(data):

    l1 = tf.add(tf.matmul(data, tf.Variable(tf.random_normal([len(train_x[0]), n_nodes_hl1]))), tf.Variable(tf.random_normal([n_nodes_hl1])))
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2]))), tf.Variable(tf.random_normal([n_nodes_hl2])))
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3]))), tf.Variable(tf.random_normal([n_nodes_hl3])))
    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3, tf.Variable(tf.random_normal([n_nodes_hl3, n_classes]))) + tf.Variable(tf.random_normal([n_classes]))

    return output


def train_neural_network(x):
    prediction = model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(prediction, y))
    optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for epoch in range(hm_epochs):
            epoch_loss = 0
            i = 0
            while i < len(train_x):
                start = i
                end = i+batch_size
                batch_x = np.array(train_x[start:end])
                batch_y = np.array(train_y[start:end])

                _, c = sess.run([optimizer, cost], feed_dict={x: batch_x,
                                                              y: batch_y})
                epoch_loss += c
                i += batch_size
            saver = tf.train.Saver()
            saver.save(sess, "./model.ckpt")
            print(epoch_loss)
        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

        print('Accuracy:', accuracy.eval({x: test_x, y: test_y}))


train_neural_network(x)


# def use_neural_network(input_data):
#     lemmatizer = WordNetLemmatizer()
#     prediction = neural_network_model(x)
#     with open('lex.data','rb') as f:
#         lexicon = pickle.load(f)

#     with tf.Session() as sess:
#         sess.run(tf.global_variables_initializer())
#         saver = tf.train.Saver()
#         saver.restore(sess,"./model.ckpt")
#         current_words = word_tokenize(input_data.lower())
#         current_words = [lemmatizer.lemmatize(i) for i in current_words]
#         features = np.zeros(len(lexicon))

#         for word in current_words:
#             if word.lower() in lexicon:
#                 index_value = lexicon.index(word.lower())
#                 # OR DO +=1, test both
#                 features[index_value] += 1

#         features = np.array(list(features))
#         # pos: [1,0] , argmax: 0
#         # neg: [0,1] , argmax: 1
#         result = (sess.run(tf.argmax(prediction.eval(feed_dict={x:[features]}),1)))
#         if result[0] == 0:
#             return 'Positive'
#         elif result[0] == 1:
#             return 'Negative'
# tw = Twitter()
# while 1:
#     print(use_neural_network(input('>>> ')))
