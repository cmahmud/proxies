# SyndProxy private pool

## Current pool

- Alive now: 1024
- Gold now: 287
- HTTP: 350 alive / 28 gold
- HTTPS: 202 alive / 4 gold
- SOCKS4: 230 alive / 139 gold
- SOCKS5: 242 alive / 116 gold

## Historical pool

- Discovered: 102805
- Ever alive: 12699
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
