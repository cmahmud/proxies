# SyndProxy private pool

## Current pool

- Alive now: 649
- Gold now: 242
- HTTP: 172 alive / 26 gold
- HTTPS: 94 alive / 7 gold
- SOCKS4: 192 alive / 120 gold
- SOCKS5: 191 alive / 89 gold

## Historical pool

- Discovered: 86742
- Ever alive: 6888
- Ever gold: 335

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
