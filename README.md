# SyndProxy private pool

## Current pool

- Alive now: 1095
- Gold now: 421
- HTTP: 324 alive / 88 gold
- HTTPS: 251 alive / 17 gold
- SOCKS4: 221 alive / 158 gold
- SOCKS5: 299 alive / 158 gold

## Historical pool

- Discovered: 134522
- Ever alive: 21838
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
