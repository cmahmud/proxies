# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 422
- HTTP: 356 alive / 86 gold
- HTTPS: 203 alive / 29 gold
- SOCKS4: 206 alive / 140 gold
- SOCKS5: 241 alive / 167 gold

## Historical pool

- Discovered: 163875
- Ever alive: 32029
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
