# SyndProxy private pool

## Current pool

- Alive now: 1109
- Gold now: 418
- HTTP: 371 alive / 96 gold
- HTTPS: 299 alive / 32 gold
- SOCKS4: 201 alive / 133 gold
- SOCKS5: 238 alive / 157 gold

## Historical pool

- Discovered: 161017
- Ever alive: 31100
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
