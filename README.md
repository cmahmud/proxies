# SyndProxy private pool

## Current pool

- Alive now: 1164
- Gold now: 532
- HTTP: 429 alive / 156 gold
- HTTPS: 324 alive / 108 gold
- SOCKS4: 217 alive / 143 gold
- SOCKS5: 194 alive / 125 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19945
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
