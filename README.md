# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 429
- HTTP: 105 alive / 70 gold
- HTTPS: 76 alive / 28 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45476
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
