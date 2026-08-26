# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 406
- HTTP: 95 alive / 64 gold
- HTTPS: 84 alive / 14 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39228
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
