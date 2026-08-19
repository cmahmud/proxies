# SyndProxy private pool

## Current pool

- Alive now: 995
- Gold now: 392
- HTTP: 285 alive / 74 gold
- HTTPS: 210 alive / 13 gold
- SOCKS4: 255 alive / 151 gold
- SOCKS5: 245 alive / 154 gold

## Historical pool

- Discovered: 129307
- Ever alive: 20401
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
