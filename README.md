# SyndProxy private pool

## Current pool

- Alive now: 1444
- Gold now: 556
- HTTP: 549 alive / 177 gold
- HTTPS: 351 alive / 86 gold
- SOCKS4: 221 alive / 139 gold
- SOCKS5: 323 alive / 154 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22712
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
