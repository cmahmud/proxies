# SyndProxy private pool

## Current pool

- Alive now: 860
- Gold now: 261
- HTTP: 241 alive / 30 gold
- HTTPS: 162 alive / 3 gold
- SOCKS4: 228 alive / 119 gold
- SOCKS5: 229 alive / 109 gold

## Historical pool

- Discovered: 99160
- Ever alive: 12099
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
