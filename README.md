# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 437
- HTTP: 135 alive / 79 gold
- HTTPS: 101 alive / 24 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34508
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
