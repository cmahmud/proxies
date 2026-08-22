# SyndProxy private pool

## Current pool

- Alive now: 930
- Gold now: 409
- HTTP: 262 alive / 93 gold
- HTTPS: 200 alive / 29 gold
- SOCKS4: 239 alive / 149 gold
- SOCKS5: 229 alive / 138 gold

## Historical pool

- Discovered: 161993
- Ever alive: 31321
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
