# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 427
- HTTP: 99 alive / 68 gold
- HTTPS: 68 alive / 27 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45476
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
