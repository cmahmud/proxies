# SyndProxy private pool

## Current pool

- Alive now: 1326
- Gold now: 521
- HTTP: 514 alive / 183 gold
- HTTPS: 351 alive / 51 gold
- SOCKS4: 211 alive / 124 gold
- SOCKS5: 250 alive / 163 gold

## Historical pool

- Discovered: 125668
- Ever alive: 19647
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
