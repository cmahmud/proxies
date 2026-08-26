# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 380
- HTTP: 86 alive / 61 gold
- HTTPS: 49 alive / 20 gold
- SOCKS4: 153 alive / 145 gold
- SOCKS5: 172 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38907
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
