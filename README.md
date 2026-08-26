# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 418
- HTTP: 110 alive / 69 gold
- HTTPS: 88 alive / 19 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38009
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
