# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 398
- HTTP: 98 alive / 62 gold
- HTTPS: 173 alive / 13 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40645
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
