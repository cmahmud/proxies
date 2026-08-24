# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 442
- HTTP: 139 alive / 87 gold
- HTTPS: 96 alive / 23 gold
- SOCKS4: 165 alive / 162 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34265
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
