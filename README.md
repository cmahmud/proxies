# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 424
- HTTP: 108 alive / 77 gold
- HTTPS: 79 alive / 19 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 179 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37914
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
