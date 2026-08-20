# SyndProxy private pool

## Current pool

- Alive now: 1539
- Gold now: 649
- HTTP: 521 alive / 217 gold
- HTTPS: 442 alive / 116 gold
- SOCKS4: 236 alive / 158 gold
- SOCKS5: 340 alive / 158 gold

## Historical pool

- Discovered: 141248
- Ever alive: 24135
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
