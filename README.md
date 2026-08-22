# SyndProxy private pool

## Current pool

- Alive now: 1058
- Gold now: 424
- HTTP: 350 alive / 92 gold
- HTTPS: 217 alive / 27 gold
- SOCKS4: 221 alive / 146 gold
- SOCKS5: 270 alive / 159 gold

## Historical pool

- Discovered: 161013
- Ever alive: 31020
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
