# SyndProxy private pool

## Current pool

- Alive now: 1119
- Gold now: 390
- HTTP: 422 alive / 83 gold
- HTTPS: 247 alive / 24 gold
- SOCKS4: 194 alive / 114 gold
- SOCKS5: 256 alive / 169 gold

## Historical pool

- Discovered: 166620
- Ever alive: 32449
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
