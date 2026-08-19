# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 549
- HTTP: 400 alive / 179 gold
- HTTPS: 275 alive / 115 gold
- SOCKS4: 195 alive / 119 gold
- SOCKS5: 205 alive / 136 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19308
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
