# SyndProxy private pool

## Current pool

- Alive now: 762
- Gold now: 409
- HTTP: 184 alive / 78 gold
- HTTPS: 149 alive / 26 gold
- SOCKS4: 213 alive / 148 gold
- SOCKS5: 216 alive / 157 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27327
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
