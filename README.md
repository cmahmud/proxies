# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 396
- HTTP: 93 alive / 51 gold
- HTTPS: 48 alive / 17 gold
- SOCKS4: 175 alive / 165 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41653
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
