# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 488
- HTTP: 150 alive / 100 gold
- HTTPS: 129 alive / 47 gold
- SOCKS4: 168 alive / 163 gold
- SOCKS5: 195 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44993
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
