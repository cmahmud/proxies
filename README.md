# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 387
- HTTP: 101 alive / 63 gold
- HTTPS: 67 alive / 22 gold
- SOCKS4: 153 alive / 145 gold
- SOCKS5: 175 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38762
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
