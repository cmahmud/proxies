# SyndProxy private pool

## Current pool

- Alive now: 759
- Gold now: 381
- HTTP: 202 alive / 69 gold
- HTTPS: 127 alive / 18 gold
- SOCKS4: 215 alive / 143 gold
- SOCKS5: 215 alive / 151 gold

## Historical pool

- Discovered: 145549
- Ever alive: 25403
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
