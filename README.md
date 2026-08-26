# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 395
- HTTP: 103 alive / 60 gold
- HTTPS: 79 alive / 12 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 192 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38277
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
