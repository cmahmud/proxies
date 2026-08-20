# SyndProxy private pool

## Current pool

- Alive now: 691
- Gold now: 361
- HTTP: 178 alive / 66 gold
- HTTPS: 142 alive / 20 gold
- SOCKS4: 183 alive / 135 gold
- SOCKS5: 188 alive / 140 gold

## Historical pool

- Discovered: 149498
- Ever alive: 26689
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
