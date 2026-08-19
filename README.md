# SyndProxy private pool

## Current pool

- Alive now: 1303
- Gold now: 433
- HTTP: 461 alive / 93 gold
- HTTPS: 314 alive / 24 gold
- SOCKS4: 229 alive / 149 gold
- SOCKS5: 299 alive / 167 gold

## Historical pool

- Discovered: 136209
- Ever alive: 22412
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
