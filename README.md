# SyndProxy private pool

## Current pool

- Alive now: 915
- Gold now: 413
- HTTP: 239 alive / 93 gold
- HTTPS: 188 alive / 22 gold
- SOCKS4: 238 alive / 150 gold
- SOCKS5: 250 alive / 148 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25205
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
