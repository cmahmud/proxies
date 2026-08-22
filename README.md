# SyndProxy private pool

## Current pool

- Alive now: 1092
- Gold now: 393
- HTTP: 401 alive / 87 gold
- HTTPS: 239 alive / 24 gold
- SOCKS4: 198 alive / 114 gold
- SOCKS5: 254 alive / 168 gold

## Historical pool

- Discovered: 166620
- Ever alive: 32449
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
