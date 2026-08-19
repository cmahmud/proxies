# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 395
- HTTP: 312 alive / 76 gold
- HTTPS: 204 alive / 14 gold
- SOCKS4: 246 alive / 144 gold
- SOCKS5: 241 alive / 161 gold

## Historical pool

- Discovered: 131100
- Ever alive: 20527
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
