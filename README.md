# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 433
- HTTP: 103 alive / 76 gold
- HTTPS: 68 alive / 28 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44425
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
