# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 201
- HTTP: 231 alive / 41 gold
- HTTPS: 88 alive / 6 gold
- SOCKS4: 93 alive / 66 gold
- SOCKS5: 148 alive / 88 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32747
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
