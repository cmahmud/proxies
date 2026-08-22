# SyndProxy private pool

## Current pool

- Alive now: 1347
- Gold now: 411
- HTTP: 561 alive / 94 gold
- HTTPS: 321 alive / 35 gold
- SOCKS4: 228 alive / 138 gold
- SOCKS5: 237 alive / 144 gold

## Historical pool

- Discovered: 163250
- Ever alive: 31727
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
