# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 406
- HTTP: 78 alive / 60 gold
- HTTPS: 55 alive / 19 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42829
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
