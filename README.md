# SyndProxy private pool

## Current pool

- Alive now: 1113
- Gold now: 402
- HTTP: 387 alive / 113 gold
- HTTPS: 255 alive / 30 gold
- SOCKS4: 228 alive / 117 gold
- SOCKS5: 243 alive / 142 gold

## Historical pool

- Discovered: 160249
- Ever alive: 30679
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
