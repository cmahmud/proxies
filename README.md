# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 379
- HTTP: 297 alive / 86 gold
- HTTPS: 167 alive / 18 gold
- SOCKS4: 198 alive / 109 gold
- SOCKS5: 248 alive / 166 gold

## Historical pool

- Discovered: 166610
- Ever alive: 32435
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
