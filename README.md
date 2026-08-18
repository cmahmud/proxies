# SyndProxy private pool

## Current pool

- Alive now: 940
- Gold now: 278
- HTTP: 328 alive / 26 gold
- HTTPS: 138 alive / 4 gold
- SOCKS4: 234 alive / 139 gold
- SOCKS5: 240 alive / 109 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12311
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
