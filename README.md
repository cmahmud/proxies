# SyndProxy private pool

## Current pool

- Alive now: 645
- Gold now: 242
- HTTP: 168 alive / 27 gold
- HTTPS: 95 alive / 8 gold
- SOCKS4: 192 alive / 119 gold
- SOCKS5: 190 alive / 88 gold

## Historical pool

- Discovered: 86742
- Ever alive: 6883
- Ever gold: 335

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
