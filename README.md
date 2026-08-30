# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 471
- HTTP: 133 alive / 94 gold
- HTTPS: 120 alive / 38 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 202 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44890
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
