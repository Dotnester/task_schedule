import ts_classes as tc

def test_init():
    """
        t1
        du1
    /   |   \
    t2  t3  t4
    du2 du3 du4
    |   |   /
    t5  t6
    du5 du6
    |   /
    t7
    du7
    """

    t1 = tc.task("t1", 10)
    t2 = tc.task("t2", 20)
    t3 = tc.task("t3", 10)
    t4 = tc.task("t4", 40)
    t5 = tc.task("t5", 10)
    t6 = tc.task("t6", 20)
    t7 = tc.task("t7", 30)
    du1 = tc.dataUnit("du1", 20)
    du2 = tc.dataUnit("du2", 20)
    du3 = tc.dataUnit("du3", 10)
    du4 = tc.dataUnit("du4", 10)
    du5 = tc.dataUnit("du5", 20)
    du6 = tc.dataUnit("du6", 10)
    du7 = tc.dataUnit("du7", 30)

    t1.addOutput(du1)
    du1.addInput(t1)

    du1.addOutput(t2)
    t2.addInput(du1)
    du1.addOutput(t3)
    t3.addInput(du1)
    du1.addOutput(t4)
    t4.addInput(du1)

    t2.addOutput(du2)
    du2.addInput(t2)
    t3.addOutput(du3)
    du3.addInput(t3)
    t4.addOutput(du4)
    du4.addInput(t4)

    du2.addOutput(t5)
    t5.addInput(du2)
    du3.addOutput(t6)
    t6.addInput(du3)
    du4.addOutput(t6)
    t6.addInput(du4)

    t5.addOutput(du5)
    du5.addInput(t5)
    t6.addOutput(du6)
    du6.addInput(t6)

    du5.addOutput(t7)
    t7.addInput(du5)
    du6.addOutput(t7)
    t7.addInput(du6)

    t7.addOutput(du7)
    du7.addInput(t7)

    assert not t1.inputs
    assert du1.outputs == [t2, t3, t4]

test_init()

