# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 430
- HTTP: 98 alive / 72 gold
- HTTPS: 64 alive / 27 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45470
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
