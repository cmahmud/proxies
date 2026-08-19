# SyndProxy private pool

## Current pool

- Alive now: 1317
- Gold now: 372
- HTTP: 414 alive / 85 gold
- HTTPS: 297 alive / 16 gold
- SOCKS4: 258 alive / 134 gold
- SOCKS5: 348 alive / 137 gold

## Historical pool

- Discovered: 133937
- Ever alive: 21472
- Ever gold: 881

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
