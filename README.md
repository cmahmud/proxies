# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 425
- HTTP: 348 alive / 111 gold
- HTTPS: 217 alive / 33 gold
- SOCKS4: 228 alive / 144 gold
- SOCKS5: 241 alive / 137 gold

## Historical pool

- Discovered: 160276
- Ever alive: 30748
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
