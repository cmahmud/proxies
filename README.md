# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 427
- HTTP: 103 alive / 78 gold
- HTTPS: 84 alive / 21 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 179 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37911
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
