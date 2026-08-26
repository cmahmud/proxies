# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 387
- HTTP: 107 alive / 63 gold
- HTTPS: 92 alive / 20 gold
- SOCKS4: 165 alive / 150 gold
- SOCKS5: 185 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39332
- Ever gold: 1298

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
