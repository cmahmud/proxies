# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 371
- HTTP: 84 alive / 45 gold
- HTTPS: 35 alive / 11 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 173048
- Ever alive: 32987
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
