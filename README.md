# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 424
- HTTP: 115 alive / 71 gold
- HTTPS: 145 alive / 20 gold
- SOCKS4: 177 alive / 165 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41278
- Ever gold: 1320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
