# SyndProxy private pool

## Current pool

- Alive now: 1209
- Gold now: 398
- HTTP: 426 alive / 89 gold
- HTTPS: 296 alive / 15 gold
- SOCKS4: 232 alive / 130 gold
- SOCKS5: 255 alive / 164 gold

## Historical pool

- Discovered: 131862
- Ever alive: 21350
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
