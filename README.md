# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 440
- HTTP: 274 alive / 100 gold
- HTTPS: 192 alive / 30 gold
- SOCKS4: 204 alive / 149 gold
- SOCKS5: 257 alive / 161 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31070
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
