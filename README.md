# SyndProxy private pool

## Current pool

- Alive now: 1112
- Gold now: 399
- HTTP: 439 alive / 87 gold
- HTTPS: 232 alive / 26 gold
- SOCKS4: 186 alive / 114 gold
- SOCKS5: 255 alive / 172 gold

## Historical pool

- Discovered: 166620
- Ever alive: 32449
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
