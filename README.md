# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 392
- HTTP: 91 alive / 52 gold
- HTTPS: 42 alive / 14 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41655
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
