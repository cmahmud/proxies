# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 433
- HTTP: 107 alive / 75 gold
- HTTPS: 70 alive / 27 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45468
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
