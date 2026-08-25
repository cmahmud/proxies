# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 399
- HTTP: 94 alive / 64 gold
- HTTPS: 70 alive / 20 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 178 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37601
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
