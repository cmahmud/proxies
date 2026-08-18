# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 261
- HTTP: 306 alive / 30 gold
- HTTPS: 167 alive / 4 gold
- SOCKS4: 238 alive / 130 gold
- SOCKS5: 201 alive / 97 gold

## Historical pool

- Discovered: 95391
- Ever alive: 10610
- Ever gold: 378

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
