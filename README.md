# SyndProxy private pool

## Current pool

- Alive now: 869
- Gold now: 378
- HTTP: 274 alive / 85 gold
- HTTPS: 159 alive / 18 gold
- SOCKS4: 192 alive / 109 gold
- SOCKS5: 244 alive / 166 gold

## Historical pool

- Discovered: 166610
- Ever alive: 32435
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
