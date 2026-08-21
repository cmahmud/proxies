# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 422
- HTTP: 331 alive / 102 gold
- HTTPS: 192 alive / 37 gold
- SOCKS4: 217 alive / 140 gold
- SOCKS5: 229 alive / 143 gold

## Historical pool

- Discovered: 160257
- Ever alive: 30698
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
