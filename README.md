# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 439
- HTTP: 123 alive / 81 gold
- HTTPS: 69 alive / 25 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 184 alive / 172 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34705
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
