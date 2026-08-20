# SyndProxy private pool

## Current pool

- Alive now: 823
- Gold now: 351
- HTTP: 216 alive / 75 gold
- HTTPS: 201 alive / 15 gold
- SOCKS4: 211 alive / 132 gold
- SOCKS5: 195 alive / 129 gold

## Historical pool

- Discovered: 149422
- Ever alive: 26543
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
