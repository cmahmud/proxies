# SyndProxy private pool

## Current pool

- Alive now: 885
- Gold now: 395
- HTTP: 228 alive / 78 gold
- HTTPS: 236 alive / 22 gold
- SOCKS4: 204 alive / 145 gold
- SOCKS5: 217 alive / 150 gold

## Historical pool

- Discovered: 148776
- Ever alive: 26505
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
