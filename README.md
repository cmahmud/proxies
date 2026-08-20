# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 406
- HTTP: 333 alive / 93 gold
- HTTPS: 270 alive / 23 gold
- SOCKS4: 203 alive / 134 gold
- SOCKS5: 225 alive / 156 gold

## Historical pool

- Discovered: 144729
- Ever alive: 24917
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
