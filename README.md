# SyndProxy private pool

## Current pool

- Alive now: 887
- Gold now: 344
- HTTP: 268 alive / 48 gold
- HTTPS: 188 alive / 14 gold
- SOCKS4: 216 alive / 134 gold
- SOCKS5: 215 alive / 148 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14923
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
