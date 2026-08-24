# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 436
- HTTP: 132 alive / 80 gold
- HTTPS: 112 alive / 23 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34532
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
