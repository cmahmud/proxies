# SyndProxy private pool

## Current pool

- Alive now: 889
- Gold now: 398
- HTTP: 290 alive / 88 gold
- HTTPS: 153 alive / 24 gold
- SOCKS4: 218 alive / 146 gold
- SOCKS5: 228 alive / 140 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29379
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
