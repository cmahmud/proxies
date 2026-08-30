# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 432
- HTTP: 123 alive / 87 gold
- HTTPS: 84 alive / 34 gold
- SOCKS4: 162 alive / 151 gold
- SOCKS5: 180 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44074
- Ever gold: 1395

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
