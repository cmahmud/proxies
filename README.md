# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 387
- HTTP: 124 alive / 69 gold
- HTTPS: 56 alive / 14 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 177 alive / 152 gold

## Historical pool

- Discovered: 176956
- Ever alive: 33250
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
