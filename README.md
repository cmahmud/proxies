# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 492
- HTTP: 149 alive / 103 gold
- HTTPS: 133 alive / 50 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 201 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44999
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
