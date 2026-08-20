# SyndProxy private pool

## Current pool

- Alive now: 1260
- Gold now: 592
- HTTP: 462 alive / 187 gold
- HTTPS: 317 alive / 97 gold
- SOCKS4: 236 alive / 147 gold
- SOCKS5: 245 alive / 161 gold

## Historical pool

- Discovered: 139662
- Ever alive: 23523
- Ever gold: 922

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
