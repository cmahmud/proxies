# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 369
- HTTP: 290 alive / 85 gold
- HTTPS: 199 alive / 21 gold
- SOCKS4: 210 alive / 128 gold
- SOCKS5: 228 alive / 135 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29823
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
