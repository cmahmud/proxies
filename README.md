# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 404
- HTTP: 285 alive / 93 gold
- HTTPS: 176 alive / 20 gold
- SOCKS4: 216 alive / 151 gold
- SOCKS5: 241 alive / 140 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29232
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
