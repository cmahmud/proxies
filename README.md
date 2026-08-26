# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 412
- HTTP: 105 alive / 67 gold
- HTTPS: 56 alive / 21 gold
- SOCKS4: 179 alive / 159 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38721
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
