# SyndProxy private pool

## Current pool

- Alive now: 946
- Gold now: 413
- HTTP: 255 alive / 93 gold
- HTTPS: 202 alive / 22 gold
- SOCKS4: 240 alive / 150 gold
- SOCKS5: 249 alive / 148 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25205
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
