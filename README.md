# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 404
- HTTP: 93 alive / 62 gold
- HTTPS: 86 alive / 15 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39273
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
