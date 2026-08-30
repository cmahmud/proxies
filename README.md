# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 452
- HTTP: 126 alive / 88 gold
- HTTPS: 52 alive / 32 gold
- SOCKS4: 165 alive / 162 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43678
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
