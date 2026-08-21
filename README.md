# SyndProxy private pool

## Current pool

- Alive now: 900
- Gold now: 402
- HTTP: 264 alive / 77 gold
- HTTPS: 168 alive / 24 gold
- SOCKS4: 228 alive / 155 gold
- SOCKS5: 240 alive / 146 gold

## Historical pool

- Discovered: 156747
- Ever alive: 29597
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
