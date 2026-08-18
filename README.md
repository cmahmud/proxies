# SyndProxy private pool

## Current pool

- Alive now: 701
- Gold now: 253
- HTTP: 167 alive / 37 gold
- HTTPS: 114 alive / 8 gold
- SOCKS4: 216 alive / 125 gold
- SOCKS5: 204 alive / 83 gold

## Historical pool

- Discovered: 94325
- Ever alive: 9350
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
