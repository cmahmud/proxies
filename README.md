# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 412
- HTTP: 101 alive / 67 gold
- HTTPS: 85 alive / 20 gold
- SOCKS4: 180 alive / 158 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38647
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
