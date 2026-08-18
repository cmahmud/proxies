# SyndProxy private pool

## Current pool

- Alive now: 832
- Gold now: 262
- HTTP: 232 alive / 30 gold
- HTTPS: 152 alive / 3 gold
- SOCKS4: 220 alive / 119 gold
- SOCKS5: 228 alive / 110 gold

## Historical pool

- Discovered: 99160
- Ever alive: 12099
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
