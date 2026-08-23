# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 347
- HTTP: 160 alive / 39 gold
- HTTPS: 47 alive / 9 gold
- SOCKS4: 186 alive / 154 gold
- SOCKS5: 221 alive / 145 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32875
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
