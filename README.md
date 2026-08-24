# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 436
- HTTP: 127 alive / 79 gold
- HTTPS: 110 alive / 23 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34489
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
