# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 529
- HTTP: 334 alive / 158 gold
- HTTPS: 270 alive / 88 gold
- SOCKS4: 228 alive / 152 gold
- SOCKS5: 200 alive / 131 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18119
- Ever gold: 715

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
