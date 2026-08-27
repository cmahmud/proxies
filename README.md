# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 416
- HTTP: 101 alive / 74 gold
- HTTPS: 100 alive / 22 gold
- SOCKS4: 163 alive / 160 gold
- SOCKS5: 175 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41835
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
