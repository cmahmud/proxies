# SyndProxy private pool

## Current pool

- Alive now: 1207
- Gold now: 461
- HTTP: 458 alive / 124 gold
- HTTPS: 275 alive / 72 gold
- SOCKS4: 217 alive / 120 gold
- SOCKS5: 257 alive / 145 gold

## Historical pool

- Discovered: 117109
- Ever alive: 17237
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
