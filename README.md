# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 405
- HTTP: 90 alive / 66 gold
- HTTPS: 80 alive / 20 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 176 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37717
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
