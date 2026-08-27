# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 407
- HTTP: 101 alive / 68 gold
- HTTPS: 174 alive / 19 gold
- SOCKS4: 177 alive / 156 gold
- SOCKS5: 190 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40606
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
