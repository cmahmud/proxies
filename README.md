# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 319
- HTTP: 320 alive / 42 gold
- HTTPS: 156 alive / 10 gold
- SOCKS4: 237 alive / 140 gold
- SOCKS5: 226 alive / 127 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14353
- Ever gold: 440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
