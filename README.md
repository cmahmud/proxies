# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 411
- HTTP: 228 alive / 90 gold
- HTTPS: 159 alive / 27 gold
- SOCKS4: 215 alive / 146 gold
- SOCKS5: 234 alive / 148 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29133
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
