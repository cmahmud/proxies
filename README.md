# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 349
- HTTP: 142 alive / 78 gold
- HTTPS: 84 alive / 30 gold
- SOCKS4: 178 alive / 63 gold
- SOCKS5: 256 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48575
- Ever gold: 1546

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
