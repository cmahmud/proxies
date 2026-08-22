# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 406
- HTTP: 265 alive / 92 gold
- HTTPS: 249 alive / 24 gold
- SOCKS4: 216 alive / 138 gold
- SOCKS5: 239 alive / 152 gold

## Historical pool

- Discovered: 164245
- Ever alive: 32075
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
