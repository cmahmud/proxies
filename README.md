# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 413
- HTTP: 334 alive / 96 gold
- HTTPS: 261 alive / 27 gold
- SOCKS4: 192 alive / 128 gold
- SOCKS5: 248 alive / 162 gold

## Historical pool

- Discovered: 143555
- Ever alive: 24892
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
