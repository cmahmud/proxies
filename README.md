# SyndProxy private pool

## Current pool

- Alive now: 829
- Gold now: 409
- HTTP: 229 alive / 89 gold
- HTTPS: 137 alive / 22 gold
- SOCKS4: 220 alive / 139 gold
- SOCKS5: 243 alive / 159 gold

## Historical pool

- Discovered: 151689
- Ever alive: 27781
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
