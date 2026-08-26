# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 404
- HTTP: 83 alive / 61 gold
- HTTPS: 58 alive / 19 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38542
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
