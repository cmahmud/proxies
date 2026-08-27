# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 412
- HTTP: 113 alive / 64 gold
- HTTPS: 166 alive / 17 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40790
- Ever gold: 1312

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
