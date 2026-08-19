# SyndProxy private pool

## Current pool

- Alive now: 1068
- Gold now: 552
- HTTP: 395 alive / 183 gold
- HTTPS: 262 alive / 113 gold
- SOCKS4: 208 alive / 117 gold
- SOCKS5: 203 alive / 139 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19303
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
