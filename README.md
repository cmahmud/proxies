# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 403
- HTTP: 105 alive / 60 gold
- HTTPS: 70 alive / 16 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38987
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
