# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 429
- HTTP: 111 alive / 81 gold
- HTTPS: 124 alive / 21 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42154
- Ever gold: 1352

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
