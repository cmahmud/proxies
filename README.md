# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 418
- HTTP: 103 alive / 70 gold
- HTTPS: 105 alive / 21 gold
- SOCKS4: 182 alive / 160 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38020
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
