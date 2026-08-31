# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 414
- HTTP: 92 alive / 62 gold
- HTTPS: 66 alive / 23 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45476
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
