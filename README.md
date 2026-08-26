# SyndProxy validated proxy pool

## Current pool

- Alive now: 676
- Gold now: 407
- HTTP: 154 alive / 72 gold
- HTTPS: 165 alive / 19 gold
- SOCKS4: 170 alive / 155 gold
- SOCKS5: 187 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40351
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
