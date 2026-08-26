# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 404
- HTTP: 92 alive / 59 gold
- HTTPS: 75 alive / 17 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39084
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
