# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 418
- HTTP: 102 alive / 69 gold
- HTTPS: 102 alive / 20 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 175 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37838
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
