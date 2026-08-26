# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 407
- HTTP: 101 alive / 63 gold
- HTTPS: 65 alive / 21 gold
- SOCKS4: 177 alive / 158 gold
- SOCKS5: 193 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38750
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
