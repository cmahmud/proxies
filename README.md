# SyndProxy private pool

## Current pool

- Alive now: 800
- Gold now: 376
- HTTP: 232 alive / 69 gold
- HTTPS: 140 alive / 18 gold
- SOCKS4: 228 alive / 146 gold
- SOCKS5: 200 alive / 143 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25494
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
