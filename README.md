# SyndProxy private pool

## Current pool

- Alive now: 748
- Gold now: 385
- HTTP: 200 alive / 78 gold
- HTTPS: 139 alive / 22 gold
- SOCKS4: 210 alive / 144 gold
- SOCKS5: 199 alive / 141 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26631
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
