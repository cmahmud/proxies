# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 431
- HTTP: 107 alive / 76 gold
- HTTPS: 63 alive / 26 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44419
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
