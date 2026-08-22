# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 409
- HTTP: 364 alive / 94 gold
- HTTPS: 233 alive / 32 gold
- SOCKS4: 215 alive / 140 gold
- SOCKS5: 228 alive / 143 gold

## Historical pool

- Discovered: 163253
- Ever alive: 31751
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
