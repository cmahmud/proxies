# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 472
- HTTP: 149 alive / 99 gold
- HTTPS: 113 alive / 35 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 196 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45128
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
