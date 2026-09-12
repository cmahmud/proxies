# SyndProxy validated proxy pool

## Current pool

- Alive now: 358
- Gold now: 297
- HTTP: 74 alive / 55 gold
- HTTPS: 27 alive / 10 gold
- SOCKS4: 112 alive / 107 gold
- SOCKS5: 145 alive / 125 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49486
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
