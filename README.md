# SyndProxy private pool

## Current pool

- Alive now: 878
- Gold now: 374
- HTTP: 273 alive / 94 gold
- HTTPS: 175 alive / 20 gold
- SOCKS4: 201 alive / 125 gold
- SOCKS5: 229 alive / 135 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29830
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
