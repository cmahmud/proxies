# SyndProxy validated proxy pool

## Current pool

- Alive now: 451
- Gold now: 359
- HTTP: 80 alive / 41 gold
- HTTPS: 27 alive / 7 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 179 alive / 157 gold

## Historical pool

- Discovered: 173056
- Ever alive: 33004
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
