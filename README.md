# SyndProxy private pool

## Current pool

- Alive now: 1193
- Gold now: 463
- HTTP: 451 alive / 124 gold
- HTTPS: 316 alive / 73 gold
- SOCKS4: 219 alive / 139 gold
- SOCKS5: 207 alive / 127 gold

## Historical pool

- Discovered: 113565
- Ever alive: 16714
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
