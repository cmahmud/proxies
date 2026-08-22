# SyndProxy private pool

## Current pool

- Alive now: 959
- Gold now: 334
- HTTP: 323 alive / 80 gold
- HTTPS: 253 alive / 25 gold
- SOCKS4: 192 alive / 139 gold
- SOCKS5: 191 alive / 90 gold

## Historical pool

- Discovered: 167096
- Ever alive: 32499
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
