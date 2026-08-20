# SyndProxy private pool

## Current pool

- Alive now: 728
- Gold now: 404
- HTTP: 168 alive / 76 gold
- HTTPS: 137 alive / 24 gold
- SOCKS4: 213 alive / 148 gold
- SOCKS5: 210 alive / 156 gold

## Historical pool

- Discovered: 151061
- Ever alive: 27333
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
