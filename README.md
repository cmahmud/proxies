# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 371
- HTTP: 97 alive / 56 gold
- HTTPS: 57 alive / 19 gold
- SOCKS4: 157 alive / 143 gold
- SOCKS5: 170 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38854
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
