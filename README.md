# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 443
- HTTP: 102 alive / 81 gold
- HTTPS: 48 alive / 29 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 180 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43686
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
