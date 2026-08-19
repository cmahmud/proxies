# SyndProxy private pool

## Current pool

- Alive now: 1329
- Gold now: 384
- HTTP: 478 alive / 88 gold
- HTTPS: 294 alive / 18 gold
- SOCKS4: 275 alive / 137 gold
- SOCKS5: 282 alive / 141 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21536
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
