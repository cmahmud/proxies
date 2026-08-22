# SyndProxy private pool

## Current pool

- Alive now: 998
- Gold now: 400
- HTTP: 315 alive / 92 gold
- HTTPS: 195 alive / 18 gold
- SOCKS4: 228 alive / 133 gold
- SOCKS5: 260 alive / 157 gold

## Historical pool

- Discovered: 166610
- Ever alive: 32433
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
