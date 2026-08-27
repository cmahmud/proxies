# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 416
- HTTP: 91 alive / 73 gold
- HTTPS: 115 alive / 20 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 176 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42048
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
