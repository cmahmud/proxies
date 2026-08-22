# SyndProxy private pool

## Current pool

- Alive now: 936
- Gold now: 395
- HTTP: 287 alive / 91 gold
- HTTPS: 192 alive / 23 gold
- SOCKS4: 198 alive / 112 gold
- SOCKS5: 259 alive / 169 gold

## Historical pool

- Discovered: 166616
- Ever alive: 32439
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
