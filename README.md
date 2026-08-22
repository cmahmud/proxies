# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 409
- HTTP: 298 alive / 83 gold
- HTTPS: 234 alive / 23 gold
- SOCKS4: 218 alive / 151 gold
- SOCKS5: 253 alive / 152 gold

## Historical pool

- Discovered: 165842
- Ever alive: 32372
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
