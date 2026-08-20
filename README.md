# SyndProxy private pool

## Current pool

- Alive now: 1254
- Gold now: 593
- HTTP: 454 alive / 188 gold
- HTTPS: 321 alive / 97 gold
- SOCKS4: 234 alive / 147 gold
- SOCKS5: 245 alive / 161 gold

## Historical pool

- Discovered: 139662
- Ever alive: 23528
- Ever gold: 922

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
