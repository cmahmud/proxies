# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 423
- HTTP: 92 alive / 63 gold
- HTTPS: 70 alive / 29 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45490
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
