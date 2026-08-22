# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 412
- HTTP: 253 alive / 90 gold
- HTTPS: 213 alive / 33 gold
- SOCKS4: 214 alive / 130 gold
- SOCKS5: 247 alive / 159 gold

## Historical pool

- Discovered: 162773
- Ever alive: 31666
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
