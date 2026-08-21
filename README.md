# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 396
- HTTP: 318 alive / 92 gold
- HTTPS: 228 alive / 30 gold
- SOCKS4: 240 alive / 143 gold
- SOCKS5: 252 alive / 131 gold

## Historical pool

- Discovered: 160990
- Ever alive: 30893
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
