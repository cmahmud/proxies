# SyndProxy private pool

## Current pool

- Alive now: 1238
- Gold now: 537
- HTTP: 456 alive / 183 gold
- HTTPS: 344 alive / 84 gold
- SOCKS4: 228 alive / 130 gold
- SOCKS5: 210 alive / 140 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19791
- Ever gold: 797

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
