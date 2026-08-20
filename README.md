# SyndProxy private pool

## Current pool

- Alive now: 720
- Gold now: 361
- HTTP: 184 alive / 81 gold
- HTTPS: 139 alive / 21 gold
- SOCKS4: 197 alive / 134 gold
- SOCKS5: 200 alive / 125 gold

## Historical pool

- Discovered: 149491
- Ever alive: 26583
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
