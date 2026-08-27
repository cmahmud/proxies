# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 402
- HTTP: 95 alive / 58 gold
- HTTPS: 104 alive / 16 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41502
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
