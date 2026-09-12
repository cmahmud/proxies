# SyndProxy validated proxy pool

## Current pool

- Alive now: 377
- Gold now: 311
- HTTP: 84 alive / 61 gold
- HTTPS: 41 alive / 22 gold
- SOCKS4: 112 alive / 102 gold
- SOCKS5: 140 alive / 126 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49508
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
