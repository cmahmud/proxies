# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 459
- HTTP: 398 alive / 125 gold
- HTTPS: 278 alive / 74 gold
- SOCKS4: 226 alive / 117 gold
- SOCKS5: 254 alive / 143 gold

## Historical pool

- Discovered: 117109
- Ever alive: 17261
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
