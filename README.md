# SyndProxy validated proxy pool

## Current pool

- Alive now: 452
- Gold now: 362
- HTTP: 88 alive / 51 gold
- HTTPS: 47 alive / 17 gold
- SOCKS4: 154 alive / 148 gold
- SOCKS5: 163 alive / 146 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43642
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
