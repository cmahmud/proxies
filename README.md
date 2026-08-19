# SyndProxy private pool

## Current pool

- Alive now: 1208
- Gold now: 386
- HTTP: 383 alive / 92 gold
- HTTPS: 309 alive / 18 gold
- SOCKS4: 233 alive / 137 gold
- SOCKS5: 283 alive / 139 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21610
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
