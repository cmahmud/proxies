# SyndProxy private pool

## Current pool

- Alive now: 973
- Gold now: 380
- HTTP: 294 alive / 80 gold
- HTTPS: 229 alive / 20 gold
- SOCKS4: 201 alive / 124 gold
- SOCKS5: 249 alive / 156 gold

## Historical pool

- Discovered: 164912
- Ever alive: 32137
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
