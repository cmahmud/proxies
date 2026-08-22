# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 426
- HTTP: 324 alive / 91 gold
- HTTPS: 212 alive / 27 gold
- SOCKS4: 229 alive / 147 gold
- SOCKS5: 272 alive / 161 gold

## Historical pool

- Discovered: 161013
- Ever alive: 31022
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
