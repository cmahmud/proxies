# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 406
- HTTP: 88 alive / 61 gold
- HTTPS: 56 alive / 19 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41713
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
