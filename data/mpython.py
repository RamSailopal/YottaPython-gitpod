import mg_python
mg_python.m_set_host(0, "localhost", 7041, "", "")
print("Setting global Test, subscript 1 to Test Entry")
mg_python.m_set(0, "^Test", 1, "Test Entry")
print('Reading ^Test(1)')
name = mg_python.m_get(0, "^Person", 1)
print(name)
