# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 436
- HTTP: 134 alive / 80 gold
- HTTPS: 105 alive / 23 gold
- SOCKS4: 181 alive / 159 gold
- SOCKS5: 192 alive / 174 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34512
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
