# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 410
- HTTP: 283 alive / 90 gold
- HTTPS: 233 alive / 29 gold
- SOCKS4: 216 alive / 139 gold
- SOCKS5: 237 alive / 152 gold

## Historical pool

- Discovered: 164245
- Ever alive: 32079
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
