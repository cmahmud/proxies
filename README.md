# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 372
- HTTP: 98 alive / 60 gold
- HTTPS: 71 alive / 16 gold
- SOCKS4: 157 alive / 143 gold
- SOCKS5: 174 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38842
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
