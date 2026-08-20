# SyndProxy private pool

## Current pool

- Alive now: 782
- Gold now: 403
- HTTP: 186 alive / 78 gold
- HTTPS: 149 alive / 25 gold
- SOCKS4: 229 alive / 155 gold
- SOCKS5: 218 alive / 145 gold

## Historical pool

- Discovered: 150516
- Ever alive: 27034
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
