# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 423
- HTTP: 112 alive / 74 gold
- HTTPS: 95 alive / 20 gold
- SOCKS4: 183 alive / 164 gold
- SOCKS5: 176 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37858
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
