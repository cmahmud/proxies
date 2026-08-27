# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 416
- HTTP: 94 alive / 64 gold
- HTTPS: 115 alive / 21 gold
- SOCKS4: 177 alive / 164 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41448
- Ever gold: 1332

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
