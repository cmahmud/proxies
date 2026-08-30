# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 484
- HTTP: 139 alive / 100 gold
- HTTPS: 116 alive / 44 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 206 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44932
- Ever gold: 1419

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
