# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 289
- HTTP: 308 alive / 29 gold
- HTTPS: 200 alive / 4 gold
- SOCKS4: 231 alive / 139 gold
- SOCKS5: 243 alive / 117 gold

## Historical pool

- Discovered: 102805
- Ever alive: 12699
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
