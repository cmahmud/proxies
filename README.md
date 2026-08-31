# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 438
- HTTP: 120 alive / 79 gold
- HTTPS: 95 alive / 25 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 204 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45458
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
