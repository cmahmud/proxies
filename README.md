# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 432
- HTTP: 125 alive / 78 gold
- HTTPS: 94 alive / 24 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34670
- Ever gold: 1257

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
