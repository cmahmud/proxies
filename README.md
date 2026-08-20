# SyndProxy private pool

## Current pool

- Alive now: 789
- Gold now: 420
- HTTP: 211 alive / 83 gold
- HTTPS: 154 alive / 23 gold
- SOCKS4: 206 alive / 151 gold
- SOCKS5: 218 alive / 163 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27399
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
