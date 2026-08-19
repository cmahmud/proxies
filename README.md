# SyndProxy private pool

## Current pool

- Alive now: 1135
- Gold now: 532
- HTTP: 419 alive / 157 gold
- HTTPS: 278 alive / 92 gold
- SOCKS4: 204 alive / 139 gold
- SOCKS5: 234 alive / 144 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18621
- Ever gold: 722

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
