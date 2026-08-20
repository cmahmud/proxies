# SyndProxy private pool

## Current pool

- Alive now: 707
- Gold now: 377
- HTTP: 161 alive / 68 gold
- HTTPS: 127 alive / 18 gold
- SOCKS4: 218 alive / 148 gold
- SOCKS5: 201 alive / 143 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26373
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
