# SyndProxy private pool

## Current pool

- Alive now: 961
- Gold now: 390
- HTTP: 328 alive / 90 gold
- HTTPS: 178 alive / 25 gold
- SOCKS4: 227 alive / 147 gold
- SOCKS5: 228 alive / 128 gold

## Historical pool

- Discovered: 165831
- Ever alive: 32352
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
