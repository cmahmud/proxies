# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 410
- HTTP: 106 alive / 68 gold
- HTTPS: 116 alive / 13 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42574
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
