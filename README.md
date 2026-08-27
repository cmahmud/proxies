# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 400
- HTTP: 78 alive / 55 gold
- HTTPS: 56 alive / 18 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41607
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
