# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 402
- HTTP: 110 alive / 65 gold
- HTTPS: 82 alive / 19 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 166 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37299
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
