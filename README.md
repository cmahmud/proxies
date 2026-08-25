# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 397
- HTTP: 100 alive / 63 gold
- HTTPS: 79 alive / 18 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 176 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37550
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
