# SyndProxy private pool

## Current pool

- Alive now: 1151
- Gold now: 539
- HTTP: 418 alive / 164 gold
- HTTPS: 291 alive / 89 gold
- SOCKS4: 218 alive / 140 gold
- SOCKS5: 224 alive / 146 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18639
- Ever gold: 722

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
