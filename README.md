# SyndProxy private pool

## Current pool

- Alive now: 1138
- Gold now: 526
- HTTP: 435 alive / 157 gold
- HTTPS: 292 alive / 90 gold
- SOCKS4: 204 alive / 136 gold
- SOCKS5: 207 alive / 143 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19864
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
