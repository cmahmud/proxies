# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 422
- HTTP: 104 alive / 72 gold
- HTTPS: 102 alive / 21 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 173 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37844
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
