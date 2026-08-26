# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 391
- HTTP: 113 alive / 68 gold
- HTTPS: 86 alive / 21 gold
- SOCKS4: 169 alive / 148 gold
- SOCKS5: 220 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39348
- Ever gold: 1298

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
