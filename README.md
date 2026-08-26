# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 407
- HTTP: 138 alive / 72 gold
- HTTPS: 159 alive / 20 gold
- SOCKS4: 168 alive / 152 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40381
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
