# SyndProxy private pool

## Current pool

- Alive now: 906
- Gold now: 365
- HTTP: 296 alive / 92 gold
- HTTPS: 184 alive / 23 gold
- SOCKS4: 200 alive / 139 gold
- SOCKS5: 226 alive / 111 gold

## Historical pool

- Discovered: 154713
- Ever alive: 28994
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
