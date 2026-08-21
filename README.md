# SyndProxy private pool

## Current pool

- Alive now: 998
- Gold now: 423
- HTTP: 336 alive / 91 gold
- HTTPS: 216 alive / 23 gold
- SOCKS4: 212 alive / 148 gold
- SOCKS5: 234 alive / 161 gold

## Historical pool

- Discovered: 156425
- Ever alive: 29500
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
