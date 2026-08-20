# SyndProxy private pool

## Current pool

- Alive now: 1005
- Gold now: 422
- HTTP: 312 alive / 96 gold
- HTTPS: 210 alive / 23 gold
- SOCKS4: 234 alive / 151 gold
- SOCKS5: 249 alive / 152 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25182
- Ever gold: 1056

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
