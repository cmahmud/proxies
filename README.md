# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 422
- HTTP: 314 alive / 87 gold
- HTTPS: 206 alive / 30 gold
- SOCKS4: 227 alive / 146 gold
- SOCKS5: 267 alive / 159 gold

## Historical pool

- Discovered: 164928
- Ever alive: 32171
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
