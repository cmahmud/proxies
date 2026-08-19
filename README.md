# SyndProxy private pool

## Current pool

- Alive now: 1244
- Gold now: 386
- HTTP: 419 alive / 91 gold
- HTTPS: 284 alive / 19 gold
- SOCKS4: 247 alive / 137 gold
- SOCKS5: 294 alive / 139 gold

## Historical pool

- Discovered: 133945
- Ever alive: 21615
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
