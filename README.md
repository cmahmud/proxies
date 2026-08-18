# SyndProxy private pool

## Current pool

- Alive now: 599
- Gold now: 194
- HTTP: 149 alive / 19 gold
- HTTPS: 89 alive / 8 gold
- SOCKS4: 167 alive / 98 gold
- SOCKS5: 194 alive / 69 gold

## Historical pool

- Discovered: 91526
- Ever alive: 8006
- Ever gold: 346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
