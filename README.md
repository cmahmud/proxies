# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 404
- HTTP: 110 alive / 60 gold
- HTTPS: 140 alive / 15 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41243
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
