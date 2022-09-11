# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHNlY3JldHMKaW1wb3J0IHJlcXVlc3RzCgpwcm94eSA9IFsiaHR0cDovLzg1LjE0LjI0My4zMTozMTI4IiwgImh0dHA6Ly8xMTMuMTk2Ljg1Ljc0OjMxMjgiLCAiaHR0cDovLzE4Mi4yNTMuMTA5LjE4Mjo4MDgwIiwgImh0dHA6Ly84LjIxOS45Ny4yNDg6ODAiLCAiaHR0cDovLzEuMjU1LjEzNC4xMzY6MzEyOCIsICJodHRwOi8vNDUuMTY3LjEyNi4yNDk6OTk5MiIsICJodHRwOi8vMTIyLjE1NS4xNjUuMTkxOjMxMjgiLCAiaHR0cDovLzMxLjE3MS4xNTQuMTk5OjgxMTgiLCAiaHR0cDovLzYyLjE3MS4xNzcuODA6MzEyOCJdCmRlZiBjbGFpbV9yZXdhcmQodG9rZW4pOgogICAgaGVhZGVycyA9IHsKICAgICdhdXRob3JpdHknOiAnYXBpLm9keXNlZS5jb20nLAogICAgJ2FjY2VwdCc6ICcqLyonLAogICAgJ2FjY2VwdC1sYW5ndWFnZSc6ICdlbi1VUyxlbjtxPTAuOScsCiAgICAnb3JpZ2luJzogJ2h0dHBzOi8vb2R5c2VlLmNvbScsCiAgICAncmVmZXJlcic6ICdodHRwczovL29keXNlZS5jb20vJywKICAgICdzZWMtY2gtdWEnOiAnIkNocm9taXVtIjt2PSIxMDQiLCAiIE5vdCBBO0JyYW5kIjt2PSI5OSIsICJHb29nbGUgQ2hyb21lIjt2PSIxMDQiJywKICAgICdzZWMtY2gtdWEtbW9iaWxlJzogJz8wJywKICAgICdzZWMtY2gtdWEtcGxhdGZvcm0nOiAnIkxpbnV4IicsCiAgICAnc2VjLWZldGNoLWRlc3QnOiAnZW1wdHknLAogICAgJ3NlYy1mZXRjaC1tb2RlJzogJ2NvcnMnLAogICAgJ3NlYy1mZXRjaC1zaXRlJzogJ3NhbWUtc2l0ZScsCiAgICAndXNlci1hZ2VudCc6ICdNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vj'
love = 'n28cVRAbpz9gMF8kZQDhZP4jYwNtH2SzLKWcYmHmAl4mAvpfPa0XPvNtVPOxLKEuVQ0trjbtVPNtVPNtVPquqKEbK3Ein2IhWmbtqT9eMJ4fPvNtVPNtVPNtW3Wyq2SlMS90rKOyWmbtW2IgLJyfK3Olo3McMTIxWljXVPNtVPNtVPNaq2SfoTI0K2SxMUWyp3ZaBvNaLxq5A3yVAREAZKI1rIcnMHMTIHWYLIuXETpmIauyMSWRHPpfPvNtVPNtVPNtW2AfLJygK2AiMTHaBvNaMGD1ZQH0LGLjZzEyLmOuMQxkAGRaYNbtVPNtsDbXVPNtVUWyp3OioaAyVQ0tpzIkqJImqUZhpT9mqPtanUE0pUZ6Yl9upTxho2E5p2IyYzAioF9lMKqupzDiL2kunJ0aYPObMJSxMKWmCJuyLJEypaZfqTygMJ91qQ02ZPjtMTS0LG1xLKEuYUOlo3ucMKZ9rjbtVPNtVPNtVPNtVPNvnUE0pPV6VPWbqUEjBv8inUqcoKIdqUWdowL0pTgeBwA0JzqdFKcABGOXEz16LxgNpzImnJEyoaEcLJjhpUWirUymL3WupTHhL29gBwtjBQNvYNbtVPNtVPNtVPNtVPNvnUE0pUZvBvNvnUE0pQbiY2u3nJ11naElnz42AUOenmbmqScanxy6GGxjFxMgrzWYDUWyp2yxMJ50nJSfYaOlo3u5p2AlLKOyYzAioGb4ZQtjVtbtVPNtVPNtVU0cPvNtVPOjpzyhqPulMKAjo25mMF5wo250MJ50XDbXMTIzVTS1qTusqT9eMJ4bXGbXVPNtVTuyLJEypaZtCFO7PvNtVPNaLKI0nT9lnKE5WmbtW2SjnF5iMUymMJHhL29gWljXVPNtVPquL2AypUDaBvNaXv8dWljXVPNtVPquL2AypUDgoTShM3IuM2HaBvNaMJ4gIIZfMJ47pG0jYwxaYNbtVPNtW2EhqPp6VPpkWljXVPNtVPqipzyanJ4aBvNanUE0pUZ6Yl9iMUymMJHhL29gWljXVPNtVPqlMJMypzIlWmbtW2u0qUOmBv8io2E5p2IyYzAioF8aYNbtVPNtW3AyLl1wnP11LFp6VPpvD2ulo21cqJ0vB3L9VwRjAPVfVPVtGz90'
god = 'IEE7QnJhbmQiO3Y9Ijk5IiwgIkdvb2dsZSBDaHJvbWUiO3Y9IjEwNCInLAogICAgJ3NlYy1jaC11YS1tb2JpbGUnOiAnPzAnLAogICAgJ3NlYy1jaC11YS1wbGF0Zm9ybSc6ICciTGludXgiJywKICAgICdzZWMtZmV0Y2gtZGVzdCc6ICdlbXB0eScsCiAgICAnc2VjLWZldGNoLW1vZGUnOiAnY29ycycsCiAgICAnc2VjLWZldGNoLXNpdGUnOiAnc2FtZS1zaXRlJywKICAgICd1c2VyLWFnZW50JzogJ01vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNC4wLjAuMCBTYWZhcmkvNTM3LjM2JywKfQoKICAgIGRhdGEgPSB7CiAgICAnYXV0aF90b2tlbic6ICcnLAogICAgJ2xhbmd1YWdlJzogJ2VuJywKICAgICdhcHBfaWQnOiAnb2R5c2VlY29tNjkyRUFXaHRvcUR1QWZRNktITVh4Rnh0OHRraG10N3NmcHJFTUhXS2p5NWhmNlB3WmNIRFY1NDJWJywKfQoKICAgIHIgPSByZXF1ZXN0cy5wb3N0KCdodHRwczovL2FwaS5vZHlzZWUuY29tL3VzZXIvbmV3JywgaGVhZGVycz1oZWFkZXJzLCBkYXRhPWRhdGEpCiAgICBkYXQgPSByLmpzb24oKQogICAgdG9rZW4xID0gZGF0WydkYXRhJ10KICAgIHRva2VuID0gdG9rZW4xWydhdXRoX3Rva2VuJ10KCiAgICByZXR1cm4gdG9rZW4KCmRlZiBjbGFpbV9yKGVtYWlsKToKICAgIHRva2VuID0gYXV0aF90b2tlbigpCiAgICBoZWFkZXJzID0gewogICAgICAgICdhdXRob3JpdHknOiAnYXBpLm9keXNlZS5jb20nLAogICAgICAgICdhY2NlcHQnOiAnKi8qJywKICAgICAgICAnYWNjZXB0LWxhbmd1YWdlJzogJ2VuLVVTLGVuO3E9MC45JywKICAgICAgICAnZG50JzogJzEnLAogICAg'
destiny = 'VPNtVPqipzyanJ4aBvNanUE0pUZ6Yl9iMUymMJHhL29gWljXVPNtVPNtVPNapzIzMKWypvp6VPqbqUEjpmbiY29xrKAyMF5wo20iWljXVPNtVPNtVPNap2IwYJAbYKIuWmbtWlWQnUWioJy1oFV7qw0vZGN0VvjtVvOBo3DtDGgPpzShMPV7qw0vBGxvYPNvE29iM2kyVRAbpz9gMFV7qw0vZGN0VvpfPvNtVPNtVPNtW3AyLl1wnP11LF1go2WcoTHaBvNaCmNaYNbtVPNtVPNtVPqmMJZgL2tgqJRgpTkuqTMipz0aBvNaVxkcoaI4VvpfPvNtVPNtVPNtW3AyLl1zMKEwnP1xMKA0WmbtW2IgpUE5WljXVPNtVPNtVPNap2IwYJMyqTAbYJ1iMTHaBvNaL29lplpfPvNtVPNtVPNtW3AyLl1zMKEwnP1mnKEyWmbtW3AuoJHgp2y0MFpfPvNtVPNtVPNtW3ImMKVgLJqyoaDaBvNaGJ96nJkfLF81YwNtXStkZGftGTyhqKttrQt2KmL0XFOOpUOfMIqyLxgcqP81ZmphZmLtXRgVIR1ZYPOfnJgyVRqyL2giXFOQnUWioJHiZGN0YwNhZP4jVSAuMzSlnF81ZmphZmLaYNbtVPNtsDbtVPNtL29in2yyplN9VUfaLKI0nS90o2gyovp6qT9eMJ59PvNtVPOjpzyhqPu0o2gyovxXVPNtVTEuqTRtCFO7PvNtVPNtVPNtW2S1qTusqT9eMJ4aBvO0o2gyovjXVPNtVPNtVPNaMJ1unJjaBvOyoJScoPjXVPNtVPNtVPNapTSmp3qipzDaBvNaHQSwn2jmK1VkL2faYNbtVPNtsDbXVPNtVUWyp3OioaAyVQ0tpzIkqJImqUZhpT9mqPtanUE0pUZ6Yl9upTxho2E5p2IyYzAioF91p2IlY3AcM25covpfVTuyLJEypaZ9nTIuMTIlplkwo29enJImCJAio2gcMKZfVTEuqTR9MTS0LFxXVPNtVUOlnJ50XUWyp3OioaAyYzAioaEyoaDcPvNtVPOwoTScoI9lMKqupzDbqT9eMJ4cPtbXV2AfLJygK3VbVxEhpzkTERWuF1ujExOuMTSgLJkcp3WuYzAioFVcPtbX'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))