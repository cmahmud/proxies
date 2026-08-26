# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 404
- HTTP: 104 alive / 63 gold
- HTTPS: 70 alive / 17 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38630
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
