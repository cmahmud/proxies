# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 404
- HTTP: 97 alive / 58 gold
- HTTPS: 103 alive / 17 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41502
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
