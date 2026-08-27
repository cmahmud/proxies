# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 421
- HTTP: 104 alive / 75 gold
- HTTPS: 137 alive / 22 gold
- SOCKS4: 177 alive / 158 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42133
- Ever gold: 1351

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
