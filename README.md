# SyndProxy private pool

## Current pool

- Alive now: 699
- Gold now: 377
- HTTP: 177 alive / 72 gold
- HTTPS: 118 alive / 20 gold
- SOCKS4: 206 alive / 146 gold
- SOCKS5: 198 alive / 139 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26365
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
