# SyndProxy private pool

## Current pool

- Alive now: 1085
- Gold now: 513
- HTTP: 383 alive / 142 gold
- HTTPS: 265 alive / 83 gold
- SOCKS4: 233 alive / 152 gold
- SOCKS5: 204 alive / 136 gold

## Historical pool

- Discovered: 119808
- Ever alive: 17979
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
