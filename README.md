# SyndProxy private pool

## Current pool

- Alive now: 765
- Gold now: 392
- HTTP: 228 alive / 90 gold
- HTTPS: 119 alive / 25 gold
- SOCKS4: 182 alive / 121 gold
- SOCKS5: 236 alive / 156 gold

## Historical pool

- Discovered: 156423
- Ever alive: 29477
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
