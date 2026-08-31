# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 431
- HTTP: 99 alive / 72 gold
- HTTPS: 72 alive / 27 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45472
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
