# SyndProxy private pool

## Current pool

- Alive now: 767
- Gold now: 397
- HTTP: 207 alive / 80 gold
- HTTPS: 130 alive / 26 gold
- SOCKS4: 196 alive / 134 gold
- SOCKS5: 234 alive / 157 gold

## Historical pool

- Discovered: 162003
- Ever alive: 31399
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
