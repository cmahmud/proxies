# SyndProxy private pool

## Current pool

- Alive now: 944
- Gold now: 296
- HTTP: 303 alive / 35 gold
- HTTPS: 201 alive / 6 gold
- SOCKS4: 222 alive / 129 gold
- SOCKS5: 218 alive / 126 gold

## Historical pool

- Discovered: 102846
- Ever alive: 13208
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
