# SyndProxy private pool

## Current pool

- Alive now: 925
- Gold now: 386
- HTTP: 301 alive / 87 gold
- HTTPS: 168 alive / 22 gold
- SOCKS4: 194 alive / 116 gold
- SOCKS5: 262 alive / 161 gold

## Historical pool

- Discovered: 166337
- Ever alive: 32396
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
