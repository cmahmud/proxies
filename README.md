# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 393
- HTTP: 87 alive / 51 gold
- HTTPS: 48 alive / 15 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41655
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
