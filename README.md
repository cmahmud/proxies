# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 444
- HTTP: 101 alive / 84 gold
- HTTPS: 50 alive / 28 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 185 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43682
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
