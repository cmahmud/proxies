# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 404
- HTTP: 100 alive / 60 gold
- HTTPS: 76 alive / 15 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38299
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
