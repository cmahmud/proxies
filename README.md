# SyndProxy private pool

## Current pool

- Alive now: 1369
- Gold now: 586
- HTTP: 483 alive / 186 gold
- HTTPS: 329 alive / 100 gold
- SOCKS4: 228 alive / 138 gold
- SOCKS5: 329 alive / 162 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23224
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
