# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 417
- HTTP: 96 alive / 70 gold
- HTTPS: 80 alive / 18 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37958
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
