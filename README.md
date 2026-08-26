# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 422
- HTTP: 106 alive / 73 gold
- HTTPS: 97 alive / 21 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 176 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37846
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
