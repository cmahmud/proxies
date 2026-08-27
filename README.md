# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 417
- HTTP: 107 alive / 76 gold
- HTTPS: 126 alive / 18 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 177 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42070
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
