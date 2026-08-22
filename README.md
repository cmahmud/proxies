# SyndProxy private pool

## Current pool

- Alive now: 1078
- Gold now: 418
- HTTP: 348 alive / 89 gold
- HTTPS: 209 alive / 30 gold
- SOCKS4: 252 alive / 145 gold
- SOCKS5: 269 alive / 154 gold

## Historical pool

- Discovered: 164927
- Ever alive: 32167
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
