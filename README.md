# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 424
- HTTP: 103 alive / 79 gold
- HTTPS: 126 alive / 20 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42142
- Ever gold: 1351

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
