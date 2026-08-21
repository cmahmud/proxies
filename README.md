# SyndProxy private pool

## Current pool

- Alive now: 883
- Gold now: 403
- HTTP: 247 alive / 87 gold
- HTTPS: 181 alive / 23 gold
- SOCKS4: 212 alive / 139 gold
- SOCKS5: 243 alive / 154 gold

## Historical pool

- Discovered: 151689
- Ever alive: 27798
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
