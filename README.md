# SyndProxy private pool

## Current pool

- Alive now: 710
- Gold now: 338
- HTTP: 188 alive / 68 gold
- HTTPS: 143 alive / 15 gold
- SOCKS4: 209 alive / 139 gold
- SOCKS5: 170 alive / 116 gold

## Historical pool

- Discovered: 145543
- Ever alive: 25358
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
