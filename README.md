# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 399
- HTTP: 273 alive / 93 gold
- HTTPS: 206 alive / 29 gold
- SOCKS4: 202 alive / 147 gold
- SOCKS5: 230 alive / 130 gold

## Historical pool

- Discovered: 161007
- Ever alive: 31001
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
