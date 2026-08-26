# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 404
- HTTP: 105 alive / 63 gold
- HTTPS: 69 alive / 20 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38714
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
