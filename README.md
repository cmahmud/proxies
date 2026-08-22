# SyndProxy private pool

## Current pool

- Alive now: 1073
- Gold now: 375
- HTTP: 380 alive / 81 gold
- HTTPS: 255 alive / 23 gold
- SOCKS4: 160 alive / 105 gold
- SOCKS5: 278 alive / 166 gold

## Historical pool

- Discovered: 166635
- Ever alive: 32469
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
