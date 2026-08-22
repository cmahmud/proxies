# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 426
- HTTP: 313 alive / 93 gold
- HTTPS: 206 alive / 27 gold
- SOCKS4: 220 alive / 147 gold
- SOCKS5: 270 alive / 159 gold

## Historical pool

- Discovered: 161013
- Ever alive: 31020
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
