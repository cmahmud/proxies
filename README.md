# SyndProxy private pool

## Current pool

- Alive now: 865
- Gold now: 211
- HTTP: 308 alive / 25 gold
- HTTPS: 186 alive / 6 gold
- SOCKS4: 220 alive / 119 gold
- SOCKS5: 151 alive / 61 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13516
- Ever gold: 420

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
