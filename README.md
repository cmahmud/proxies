# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 401
- HTTP: 98 alive / 64 gold
- HTTPS: 84 alive / 19 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 179 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37568
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
