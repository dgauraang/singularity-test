if __name__ == '__main__':
    actor = None

    for i in range(1000):
        with open('/actor/current_actor.pt', 'r') as actor_file:
            actor = actor_file.read()
        with open('/buffer/exp', 'a') as exp_file:
            exp.write(actor)
