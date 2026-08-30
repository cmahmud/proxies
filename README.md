# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 459
- HTTP: 124 alive / 91 gold
- HTTPS: 102 alive / 35 gold
- SOCKS4: 163 alive / 159 gold
- SOCKS5: 196 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44795
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
