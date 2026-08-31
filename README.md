# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 425
- HTTP: 90 alive / 64 gold
- HTTPS: 62 alive / 30 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45491
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
