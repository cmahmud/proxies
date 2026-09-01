# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 469
- HTTP: 138 alive / 95 gold
- HTTPS: 110 alive / 36 gold
- SOCKS4: 178 alive / 164 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46886
- Ever gold: 1455

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
