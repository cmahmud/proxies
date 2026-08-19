# SyndProxy private pool

## Current pool

- Alive now: 1119
- Gold now: 525
- HTTP: 425 alive / 158 gold
- HTTPS: 287 alive / 89 gold
- SOCKS4: 200 alive / 135 gold
- SOCKS5: 207 alive / 143 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19864
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
