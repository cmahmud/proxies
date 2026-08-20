# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 413
- HTTP: 305 alive / 92 gold
- HTTPS: 260 alive / 26 gold
- SOCKS4: 237 alive / 150 gold
- SOCKS5: 251 alive / 145 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25204
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
