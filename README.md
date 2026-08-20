# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 403
- HTTP: 355 alive / 91 gold
- HTTPS: 260 alive / 24 gold
- SOCKS4: 204 alive / 134 gold
- SOCKS5: 222 alive / 154 gold

## Historical pool

- Discovered: 144729
- Ever alive: 24919
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
