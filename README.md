# SyndProxy private pool

## Current pool

- Alive now: 888
- Gold now: 363
- HTTP: 280 alive / 88 gold
- HTTPS: 199 alive / 17 gold
- SOCKS4: 210 alive / 142 gold
- SOCKS5: 199 alive / 116 gold

## Historical pool

- Discovered: 119837
- Ever alive: 18360
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
