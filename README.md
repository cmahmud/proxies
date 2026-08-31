# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 429
- HTTP: 104 alive / 70 gold
- HTTPS: 74 alive / 28 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 192 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45475
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
