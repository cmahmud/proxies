# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 322
- HTTP: 351 alive / 44 gold
- HTTPS: 214 alive / 11 gold
- SOCKS4: 243 alive / 137 gold
- SOCKS5: 237 alive / 130 gold

## Historical pool

- Discovered: 107044
- Ever alive: 14409
- Ever gold: 447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
