# SyndProxy validated proxy pool

## Current pool

- Alive now: 674
- Gold now: 402
- HTTP: 139 alive / 80 gold
- HTTPS: 190 alive / 23 gold
- SOCKS4: 170 alive / 146 gold
- SOCKS5: 175 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39959
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
