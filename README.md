# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 423
- HTTP: 86 alive / 61 gold
- HTTPS: 65 alive / 33 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45491
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
