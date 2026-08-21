# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 394
- HTTP: 299 alive / 77 gold
- HTTPS: 222 alive / 24 gold
- SOCKS4: 228 alive / 144 gold
- SOCKS5: 233 alive / 149 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29578
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
