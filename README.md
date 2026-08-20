# SyndProxy private pool

## Current pool

- Alive now: 1303
- Gold now: 590
- HTTP: 437 alive / 189 gold
- HTTPS: 297 alive / 100 gold
- SOCKS4: 228 alive / 138 gold
- SOCKS5: 341 alive / 163 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23228
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
