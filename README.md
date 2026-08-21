# SyndProxy private pool

## Current pool

- Alive now: 1145
- Gold now: 400
- HTTP: 418 alive / 101 gold
- HTTPS: 235 alive / 23 gold
- SOCKS4: 228 alive / 130 gold
- SOCKS5: 264 alive / 146 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27953
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
