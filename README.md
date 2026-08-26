# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 422
- HTTP: 104 alive / 72 gold
- HTTPS: 103 alive / 21 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 174 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37843
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
