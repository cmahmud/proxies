# SyndProxy private pool

## Current pool

- Alive now: 778
- Gold now: 390
- HTTP: 245 alive / 86 gold
- HTTPS: 128 alive / 22 gold
- SOCKS4: 180 alive / 123 gold
- SOCKS5: 225 alive / 159 gold

## Historical pool

- Discovered: 156418
- Ever alive: 29473
- Ever gold: 1128

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
