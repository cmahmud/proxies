# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 205
- HTTP: 242 alive / 44 gold
- HTTPS: 52 alive / 6 gold
- SOCKS4: 97 alive / 67 gold
- SOCKS5: 151 alive / 88 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32739
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
