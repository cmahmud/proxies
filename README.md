# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 371
- HTTP: 81 alive / 44 gold
- HTTPS: 35 alive / 12 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 175 alive / 158 gold

## Historical pool

- Discovered: 173029
- Ever alive: 32987
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
