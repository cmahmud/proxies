# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 404
- HTTP: 78 alive / 60 gold
- HTTPS: 58 alive / 21 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42801
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
