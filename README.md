# SyndProxy private pool

## Current pool

- Alive now: 1275
- Gold now: 419
- HTTP: 405 alive / 86 gold
- HTTPS: 330 alive / 17 gold
- SOCKS4: 229 alive / 157 gold
- SOCKS5: 311 alive / 159 gold

## Historical pool

- Discovered: 134522
- Ever alive: 21833
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
