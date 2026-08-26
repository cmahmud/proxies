# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 394
- HTTP: 133 alive / 74 gold
- HTTPS: 186 alive / 22 gold
- SOCKS4: 166 alive / 146 gold
- SOCKS5: 170 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39937
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
