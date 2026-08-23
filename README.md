# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 370
- HTTP: 80 alive / 44 gold
- HTTPS: 34 alive / 11 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 176 alive / 159 gold

## Historical pool

- Discovered: 173048
- Ever alive: 32987
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
