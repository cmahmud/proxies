# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 524
- HTTP: 367 alive / 157 gold
- HTTPS: 263 alive / 94 gold
- SOCKS4: 184 alive / 133 gold
- SOCKS5: 201 alive / 140 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19894
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
