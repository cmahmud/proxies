# SyndProxy private pool

## Current pool

- Alive now: 952
- Gold now: 334
- HTTP: 322 alive / 82 gold
- HTTPS: 227 alive / 29 gold
- SOCKS4: 207 alive / 136 gold
- SOCKS5: 196 alive / 87 gold

## Historical pool

- Discovered: 167104
- Ever alive: 32513
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
