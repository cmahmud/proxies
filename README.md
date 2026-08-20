# SyndProxy private pool

## Current pool

- Alive now: 721
- Gold now: 389
- HTTP: 156 alive / 80 gold
- HTTPS: 122 alive / 19 gold
- SOCKS4: 228 alive / 146 gold
- SOCKS5: 215 alive / 144 gold

## Historical pool

- Discovered: 144748
- Ever alive: 25211
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
