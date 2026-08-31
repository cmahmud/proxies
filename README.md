# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 425
- HTTP: 92 alive / 68 gold
- HTTPS: 66 alive / 28 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 194 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45478
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
