# SyndProxy private pool

## Current pool

- Alive now: 731
- Gold now: 387
- HTTP: 184 alive / 77 gold
- HTTPS: 122 alive / 20 gold
- SOCKS4: 211 alive / 139 gold
- SOCKS5: 214 alive / 151 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25504
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
