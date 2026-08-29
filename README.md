# SyndProxy validated proxy pool

## Current pool

- Alive now: 418
- Gold now: 349
- HTTP: 50 alive / 37 gold
- HTTPS: 31 alive / 4 gold
- SOCKS4: 161 alive / 154 gold
- SOCKS5: 176 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43563
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
