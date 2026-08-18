# SyndProxy private pool

## Current pool

- Alive now: 1028
- Gold now: 281
- HTTP: 362 alive / 35 gold
- HTTPS: 216 alive / 5 gold
- SOCKS4: 232 alive / 136 gold
- SOCKS5: 218 alive / 105 gold

## Historical pool

- Discovered: 99074
- Ever alive: 11409
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
