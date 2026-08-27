# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 402
- HTTP: 108 alive / 63 gold
- HTTPS: 174 alive / 13 gold
- SOCKS4: 186 alive / 161 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40912
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
