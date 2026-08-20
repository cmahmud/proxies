# SyndProxy private pool

## Current pool

- Alive now: 1516
- Gold now: 586
- HTTP: 651 alive / 198 gold
- HTTPS: 387 alive / 97 gold
- SOCKS4: 230 alive / 141 gold
- SOCKS5: 248 alive / 150 gold

## Historical pool

- Discovered: 136252
- Ever alive: 22774
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
