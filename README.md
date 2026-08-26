# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 370
- HTTP: 93 alive / 56 gold
- HTTPS: 59 alive / 18 gold
- SOCKS4: 157 alive / 143 gold
- SOCKS5: 173 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38890
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
