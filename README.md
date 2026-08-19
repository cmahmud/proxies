# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 511
- HTTP: 325 alive / 149 gold
- HTTPS: 231 alive / 89 gold
- SOCKS4: 219 alive / 144 gold
- SOCKS5: 207 alive / 129 gold

## Historical pool

- Discovered: 117160
- Ever alive: 17657
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
