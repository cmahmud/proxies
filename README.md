# SyndProxy private pool

## Current pool

- Alive now: 926
- Gold now: 403
- HTTP: 275 alive / 90 gold
- HTTPS: 168 alive / 18 gold
- SOCKS4: 235 alive / 136 gold
- SOCKS5: 248 alive / 159 gold

## Historical pool

- Discovered: 166610
- Ever alive: 32434
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
