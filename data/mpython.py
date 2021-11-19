import mg_python
mg_python.m_set_host(0, "localhost", 7041, "", "")
print("Setting Up MOVIE global entry for hello world...")
mg_python.m_set(0, "^MOVIE", "hello world", "")
print('Reading ^Test(1)...')
name = mg_python.m_get(0, "^Test", 1)
print(name)
