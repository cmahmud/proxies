# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 421
- HTTP: 146 alive / 80 gold
- HTTPS: 158 alive / 25 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 186 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40291
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
