# SyndProxy private pool

## Current pool

- Alive now: 1087
- Gold now: 404
- HTTP: 318 alive / 93 gold
- HTTPS: 236 alive / 15 gold
- SOCKS4: 249 alive / 147 gold
- SOCKS5: 284 alive / 149 gold

## Historical pool

- Discovered: 131828
- Ever alive: 21084
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
