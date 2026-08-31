# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 481
- HTTP: 146 alive / 98 gold
- HTTPS: 133 alive / 46 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 201 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45016
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
