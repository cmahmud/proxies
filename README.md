# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 419
- HTTP: 102 alive / 63 gold
- HTTPS: 87 alive / 20 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 200 alive / 176 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35985
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
