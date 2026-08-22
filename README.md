# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 409
- HTTP: 317 alive / 94 gold
- HTTPS: 174 alive / 31 gold
- SOCKS4: 201 alive / 145 gold
- SOCKS5: 222 alive / 139 gold

## Historical pool

- Discovered: 167119
- Ever alive: 32532
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
