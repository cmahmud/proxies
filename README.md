# SyndProxy private pool

## Current pool

- Alive now: 958
- Gold now: 370
- HTTP: 309 alive / 68 gold
- HTTPS: 210 alive / 19 gold
- SOCKS4: 211 alive / 143 gold
- SOCKS5: 228 alive / 140 gold

## Historical pool

- Discovered: 149502
- Ever alive: 26718
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
