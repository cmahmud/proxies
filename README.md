# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 402
- HTTP: 106 alive / 59 gold
- HTTPS: 70 alive / 14 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 199 alive / 170 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38288
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
