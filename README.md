# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 409
- HTTP: 101 alive / 65 gold
- HTTPS: 81 alive / 19 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 175 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37808
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
