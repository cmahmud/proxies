# SyndProxy private pool

## Current pool

- Alive now: 739
- Gold now: 404
- HTTP: 163 alive / 75 gold
- HTTPS: 133 alive / 23 gold
- SOCKS4: 224 alive / 151 gold
- SOCKS5: 219 alive / 155 gold

## Historical pool

- Discovered: 151061
- Ever alive: 27342
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
