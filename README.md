# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 410
- HTTP: 120 alive / 70 gold
- HTTPS: 166 alive / 16 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40539
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
