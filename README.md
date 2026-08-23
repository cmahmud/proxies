# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 348
- HTTP: 141 alive / 40 gold
- HTTPS: 50 alive / 9 gold
- SOCKS4: 190 alive / 154 gold
- SOCKS5: 219 alive / 145 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32875
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
