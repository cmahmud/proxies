# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 380
- HTTP: 120 alive / 70 gold
- HTTPS: 68 alive / 20 gold
- SOCKS4: 146 alive / 140 gold
- SOCKS5: 172 alive / 150 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38768
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
