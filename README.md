# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 259
- HTTP: 318 alive / 29 gold
- HTTPS: 163 alive / 10 gold
- SOCKS4: 229 alive / 119 gold
- SOCKS5: 235 alive / 101 gold

## Historical pool

- Discovered: 94373
- Ever alive: 10175
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
