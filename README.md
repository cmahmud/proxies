# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 405
- HTTP: 85 alive / 61 gold
- HTTPS: 52 alive / 17 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41644
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
