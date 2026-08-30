# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 472
- HTTP: 141 alive / 95 gold
- HTTPS: 113 alive / 40 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 198 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44925
- Ever gold: 1419

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
