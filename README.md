# SyndProxy private pool

## Current pool

- Alive now: 980
- Gold now: 440
- HTTP: 304 alive / 95 gold
- HTTPS: 204 alive / 33 gold
- SOCKS4: 212 alive / 146 gold
- SOCKS5: 260 alive / 166 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31050
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
