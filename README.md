# SyndProxy private pool

## Current pool

- Alive now: 837
- Gold now: 385
- HTTP: 259 alive / 78 gold
- HTTPS: 191 alive / 26 gold
- SOCKS4: 186 alive / 130 gold
- SOCKS5: 201 alive / 151 gold

## Historical pool

- Discovered: 161996
- Ever alive: 31346
- Ever gold: 1158

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
