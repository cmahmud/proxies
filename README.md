# SyndProxy validated proxy pool

## Current pool

- Alive now: 366
- Gold now: 320
- HTTP: 51 alive / 31 gold
- HTTPS: 15 alive / 0 gold
- SOCKS4: 148 alive / 145 gold
- SOCKS5: 152 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43631
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
