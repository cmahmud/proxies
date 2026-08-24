# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 416
- HTTP: 136 alive / 71 gold
- HTTPS: 80 alive / 19 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33831
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
