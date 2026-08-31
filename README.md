# SyndProxy validated proxy pool

## Current pool

- Alive now: 699
- Gold now: 469
- HTTP: 161 alive / 95 gold
- HTTPS: 134 alive / 37 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 236 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45275
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
