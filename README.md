# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 408
- HTTP: 105 alive / 66 gold
- HTTPS: 177 alive / 19 gold
- SOCKS4: 178 alive / 157 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40612
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
