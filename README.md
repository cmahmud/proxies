# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 399
- HTTP: 292 alive / 93 gold
- HTTPS: 186 alive / 29 gold
- SOCKS4: 236 alive / 147 gold
- SOCKS5: 236 alive / 130 gold

## Historical pool

- Discovered: 161006
- Ever alive: 30991
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
