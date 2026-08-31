# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 479
- HTTP: 149 alive / 96 gold
- HTTPS: 129 alive / 46 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 201 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45016
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
