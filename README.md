# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 419
- HTTP: 95 alive / 58 gold
- HTTPS: 72 alive / 33 gold
- SOCKS4: 187 alive / 160 gold
- SOCKS5: 194 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45493
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
