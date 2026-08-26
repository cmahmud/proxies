# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 403
- HTTP: 101 alive / 60 gold
- HTTPS: 79 alive / 15 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 197 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38299
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
