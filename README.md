# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 360
- HTTP: 307 alive / 70 gold
- HTTPS: 243 alive / 18 gold
- SOCKS4: 229 alive / 153 gold
- SOCKS5: 230 alive / 119 gold

## Historical pool

- Discovered: 111009
- Ever alive: 16104
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
