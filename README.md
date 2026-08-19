# SyndProxy private pool

## Current pool

- Alive now: 1207
- Gold now: 355
- HTTP: 393 alive / 85 gold
- HTTPS: 266 alive / 22 gold
- SOCKS4: 228 alive / 112 gold
- SOCKS5: 320 alive / 136 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22055
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
