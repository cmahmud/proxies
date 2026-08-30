# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 425
- HTTP: 107 alive / 72 gold
- HTTPS: 70 alive / 24 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44377
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
