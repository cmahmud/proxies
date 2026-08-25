# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 397
- HTTP: 100 alive / 67 gold
- HTTPS: 83 alive / 18 gold
- SOCKS4: 164 alive / 156 gold
- SOCKS5: 171 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37430
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
