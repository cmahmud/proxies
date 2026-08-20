# SyndProxy private pool

## Current pool

- Alive now: 1268
- Gold now: 562
- HTTP: 458 alive / 190 gold
- HTTPS: 348 alive / 94 gold
- SOCKS4: 240 alive / 145 gold
- SOCKS5: 222 alive / 133 gold

## Historical pool

- Discovered: 137899
- Ever alive: 22925
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
