# SyndProxy private pool

## Current pool

- Alive now: 886
- Gold now: 296
- HTTP: 273 alive / 50 gold
- HTTPS: 173 alive / 10 gold
- SOCKS4: 224 alive / 109 gold
- SOCKS5: 216 alive / 127 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14448
- Ever gold: 464

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
