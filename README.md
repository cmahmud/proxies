# SyndProxy private pool

## Current pool

- Alive now: 748
- Gold now: 334
- HTTP: 224 alive / 90 gold
- HTTPS: 133 alive / 27 gold
- SOCKS4: 163 alive / 94 gold
- SOCKS5: 228 alive / 123 gold

## Historical pool

- Discovered: 167408
- Ever alive: 32570
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
