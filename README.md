# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 493
- HTTP: 141 alive / 103 gold
- HTTPS: 140 alive / 52 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 200 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45007
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
