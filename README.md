# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 441
- HTTP: 318 alive / 92 gold
- HTTPS: 207 alive / 27 gold
- SOCKS4: 231 alive / 149 gold
- SOCKS5: 276 alive / 173 gold

## Historical pool

- Discovered: 161013
- Ever alive: 31024
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
