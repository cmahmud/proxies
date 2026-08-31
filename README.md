# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 448
- HTTP: 139 alive / 78 gold
- HTTPS: 99 alive / 35 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 216 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45417
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
