# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 417
- HTTP: 102 alive / 62 gold
- HTTPS: 78 alive / 24 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35795
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
