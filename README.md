# SyndProxy private pool

## Current pool

- Alive now: 724
- Gold now: 374
- HTTP: 193 alive / 67 gold
- HTTPS: 135 alive / 22 gold
- SOCKS4: 201 alive / 146 gold
- SOCKS5: 195 alive / 139 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26351
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
