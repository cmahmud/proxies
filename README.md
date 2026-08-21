# SyndProxy private pool

## Current pool

- Alive now: 1095
- Gold now: 426
- HTTP: 370 alive / 114 gold
- HTTPS: 244 alive / 29 gold
- SOCKS4: 236 alive / 140 gold
- SOCKS5: 245 alive / 143 gold

## Historical pool

- Discovered: 160253
- Ever alive: 30683
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
