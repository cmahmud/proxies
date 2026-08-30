# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 441
- HTTP: 127 alive / 86 gold
- HTTPS: 72 alive / 29 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44292
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
