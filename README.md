# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 397
- HTTP: 88 alive / 54 gold
- HTTPS: 51 alive / 17 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41648
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
