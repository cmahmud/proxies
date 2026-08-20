# SyndProxy private pool

## Current pool

- Alive now: 746
- Gold now: 406
- HTTP: 173 alive / 76 gold
- HTTPS: 142 alive / 24 gold
- SOCKS4: 215 alive / 148 gold
- SOCKS5: 216 alive / 158 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27331
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
