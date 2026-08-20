# SyndProxy private pool

## Current pool

- Alive now: 1238
- Gold now: 436
- HTTP: 403 alive / 103 gold
- HTTPS: 305 alive / 26 gold
- SOCKS4: 269 alive / 150 gold
- SOCKS5: 261 alive / 157 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25163
- Ever gold: 1056

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
