# SyndProxy validated proxy pool

## Current pool

- Alive now: 358
- Gold now: 314
- HTTP: 74 alive / 61 gold
- HTTPS: 33 alive / 22 gold
- SOCKS4: 112 alive / 104 gold
- SOCKS5: 139 alive / 127 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49500
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
