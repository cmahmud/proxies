# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 411
- HTTP: 120 alive / 62 gold
- HTTPS: 148 alive / 21 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41312
- Ever gold: 1324

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
