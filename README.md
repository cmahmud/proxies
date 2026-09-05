# SyndProxy validated proxy pool

## Current pool

- Alive now: 379
- Gold now: 288
- HTTP: 106 alive / 75 gold
- HTTPS: 40 alive / 19 gold
- SOCKS4: 73 alive / 61 gold
- SOCKS5: 160 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47850
- Ever gold: 1498

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
