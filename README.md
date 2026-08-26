# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 407
- HTTP: 110 alive / 63 gold
- HTTPS: 57 alive / 21 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38734
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
