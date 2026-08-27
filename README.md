# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 400
- HTTP: 90 alive / 54 gold
- HTTPS: 54 alive / 20 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41696
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
