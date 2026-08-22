# SyndProxy private pool

## Current pool

- Alive now: 943
- Gold now: 403
- HTTP: 260 alive / 90 gold
- HTTPS: 230 alive / 24 gold
- SOCKS4: 218 alive / 138 gold
- SOCKS5: 235 alive / 151 gold

## Historical pool

- Discovered: 164245
- Ever alive: 32072
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
