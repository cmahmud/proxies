# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 409
- HTTP: 309 alive / 95 gold
- HTTPS: 229 alive / 33 gold
- SOCKS4: 225 alive / 146 gold
- SOCKS5: 240 alive / 135 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30970
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
