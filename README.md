# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 416
- HTTP: 102 alive / 67 gold
- HTTPS: 109 alive / 21 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41460
- Ever gold: 1332

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
