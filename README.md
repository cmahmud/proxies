# SyndProxy private pool

## Current pool

- Alive now: 815
- Gold now: 379
- HTTP: 194 alive / 75 gold
- HTTPS: 185 alive / 19 gold
- SOCKS4: 220 alive / 147 gold
- SOCKS5: 216 alive / 138 gold

## Historical pool

- Discovered: 149510
- Ever alive: 26899
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
