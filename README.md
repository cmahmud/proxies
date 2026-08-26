# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 397
- HTTP: 104 alive / 60 gold
- HTTPS: 88 alive / 12 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 192 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38348
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
