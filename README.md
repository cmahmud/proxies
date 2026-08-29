# SyndProxy validated proxy pool

## Current pool

- Alive now: 395
- Gold now: 331
- HTTP: 72 alive / 36 gold
- HTTPS: 21 alive / 5 gold
- SOCKS4: 154 alive / 146 gold
- SOCKS5: 148 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43634
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
