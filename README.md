# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 387
- HTTP: 127 alive / 71 gold
- HTTPS: 169 alive / 19 gold
- SOCKS4: 160 alive / 146 gold
- SOCKS5: 177 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39891
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
