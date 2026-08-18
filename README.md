# SyndProxy private pool

## Current pool

- Alive now: 915
- Gold now: 251
- HTTP: 347 alive / 29 gold
- HTTPS: 160 alive / 5 gold
- SOCKS4: 210 alive / 123 gold
- SOCKS5: 198 alive / 94 gold

## Historical pool

- Discovered: 95391
- Ever alive: 10610
- Ever gold: 378

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
