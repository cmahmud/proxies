# SyndProxy private pool

## Current pool

- Alive now: 921
- Gold now: 412
- HTTP: 323 alive / 95 gold
- HTTPS: 170 alive / 31 gold
- SOCKS4: 203 alive / 147 gold
- SOCKS5: 225 alive / 139 gold

## Historical pool

- Discovered: 167119
- Ever alive: 32530
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
