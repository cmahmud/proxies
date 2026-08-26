# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 422
- HTTP: 120 alive / 76 gold
- HTTPS: 72 alive / 19 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 176 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37918
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
