# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 404
- HTTP: 90 alive / 60 gold
- HTTPS: 54 alive / 17 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41645
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
