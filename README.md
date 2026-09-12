# SyndProxy validated proxy pool

## Current pool

- Alive now: 377
- Gold now: 310
- HTTP: 83 alive / 64 gold
- HTTPS: 38 alive / 20 gold
- SOCKS4: 112 alive / 102 gold
- SOCKS5: 144 alive / 124 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49490
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
