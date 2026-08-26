# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 407
- HTTP: 117 alive / 64 gold
- HTTPS: 73 alive / 15 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38412
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
