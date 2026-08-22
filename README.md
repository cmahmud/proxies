# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 366
- HTTP: 326 alive / 78 gold
- HTTPS: 213 alive / 22 gold
- SOCKS4: 203 alive / 125 gold
- SOCKS5: 229 alive / 141 gold

## Historical pool

- Discovered: 165812
- Ever alive: 32318
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
