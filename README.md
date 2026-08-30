# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 484
- HTTP: 156 alive / 102 gold
- HTTPS: 120 alive / 43 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 202 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44976
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
