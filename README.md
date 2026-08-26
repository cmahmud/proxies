# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 417
- HTTP: 127 alive / 79 gold
- HTTPS: 150 alive / 22 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40239
- Ever gold: 1308

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
