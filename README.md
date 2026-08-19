# SyndProxy private pool

## Current pool

- Alive now: 1586
- Gold now: 437
- HTTP: 579 alive / 97 gold
- HTTPS: 398 alive / 25 gold
- SOCKS4: 274 alive / 148 gold
- SOCKS5: 335 alive / 167 gold

## Historical pool

- Discovered: 136220
- Ever alive: 22466
- Ever gold: 907

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
