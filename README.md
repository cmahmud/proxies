# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 397
- HTTP: 87 alive / 57 gold
- HTTPS: 68 alive / 16 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38497
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
