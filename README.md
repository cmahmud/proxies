# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 398
- HTTP: 332 alive / 74 gold
- HTTPS: 224 alive / 16 gold
- SOCKS4: 258 alive / 148 gold
- SOCKS5: 234 alive / 160 gold

## Historical pool

- Discovered: 129319
- Ever alive: 20464
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
