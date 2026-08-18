# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 342
- HTTP: 395 alive / 51 gold
- HTTPS: 201 alive / 10 gold
- SOCKS4: 234 alive / 143 gold
- SOCKS5: 215 alive / 138 gold

## Historical pool

- Discovered: 107060
- Ever alive: 14641
- Ever gold: 467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
