# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 421
- HTTP: 132 alive / 81 gold
- HTTPS: 76 alive / 30 gold
- SOCKS4: 157 alive / 151 gold
- SOCKS5: 234 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43955
- Ever gold: 1381

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
