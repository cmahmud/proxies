# SyndProxy private pool

## Current pool

- Alive now: 1154
- Gold now: 409
- HTTP: 407 alive / 108 gold
- HTTPS: 289 alive / 28 gold
- SOCKS4: 248 alive / 151 gold
- SOCKS5: 210 alive / 122 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30594
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
