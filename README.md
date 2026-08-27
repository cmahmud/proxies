# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 396
- HTTP: 96 alive / 52 gold
- HTTPS: 48 alive / 16 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41652
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
