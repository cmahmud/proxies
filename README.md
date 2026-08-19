# SyndProxy private pool

## Current pool

- Alive now: 1149
- Gold now: 395
- HTTP: 380 alive / 87 gold
- HTTPS: 291 alive / 15 gold
- SOCKS4: 226 alive / 130 gold
- SOCKS5: 252 alive / 163 gold

## Historical pool

- Discovered: 131860
- Ever alive: 21341
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
