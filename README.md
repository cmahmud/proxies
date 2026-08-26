# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 404
- HTTP: 95 alive / 65 gold
- HTTPS: 72 alive / 18 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 189 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38675
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
