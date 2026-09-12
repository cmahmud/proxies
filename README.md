# SyndProxy validated proxy pool

## Current pool

- Alive now: 396
- Gold now: 319
- HTTP: 94 alive / 67 gold
- HTTPS: 37 alive / 18 gold
- SOCKS4: 126 alive / 105 gold
- SOCKS5: 139 alive / 129 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49536
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
