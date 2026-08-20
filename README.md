# SyndProxy private pool

## Current pool

- Alive now: 684
- Gold now: 379
- HTTP: 165 alive / 70 gold
- HTTPS: 89 alive / 14 gold
- SOCKS4: 201 alive / 137 gold
- SOCKS5: 229 alive / 158 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25792
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
