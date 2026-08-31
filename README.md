# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 427
- HTTP: 99 alive / 68 gold
- HTTPS: 69 alive / 27 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45476
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
