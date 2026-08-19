# SyndProxy private pool

## Current pool

- Alive now: 1101
- Gold now: 470
- HTTP: 359 alive / 121 gold
- HTTPS: 280 alive / 73 gold
- SOCKS4: 228 alive / 138 gold
- SOCKS5: 234 alive / 138 gold

## Historical pool

- Discovered: 113538
- Ever alive: 16585
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
