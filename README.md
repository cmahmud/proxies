# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 385
- HTTP: 105 alive / 65 gold
- HTTPS: 59 alive / 19 gold
- SOCKS4: 153 alive / 145 gold
- SOCKS5: 174 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38915
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
