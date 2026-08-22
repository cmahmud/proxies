# SyndProxy private pool

## Current pool

- Alive now: 831
- Gold now: 389
- HTTP: 221 alive / 90 gold
- HTTPS: 180 alive / 28 gold
- SOCKS4: 214 alive / 139 gold
- SOCKS5: 216 alive / 132 gold

## Historical pool

- Discovered: 162766
- Ever alive: 31635
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
