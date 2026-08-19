# SyndProxy private pool

## Current pool

- Alive now: 1298
- Gold now: 394
- HTTP: 412 alive / 93 gold
- HTTPS: 282 alive / 17 gold
- SOCKS4: 234 alive / 124 gold
- SOCKS5: 370 alive / 160 gold

## Historical pool

- Discovered: 133936
- Ever alive: 21461
- Ever gold: 881

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
