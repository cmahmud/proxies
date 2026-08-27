# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 403
- HTTP: 94 alive / 58 gold
- HTTPS: 105 alive / 16 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41502
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
