# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 400
- HTTP: 98 alive / 58 gold
- HTTPS: 74 alive / 16 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39021
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
