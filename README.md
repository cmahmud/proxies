# SyndProxy validated proxy pool

## Current pool

- Alive now: 358
- Gold now: 335
- HTTP: 35 alive / 25 gold
- HTTPS: 4 alive / 0 gold
- SOCKS4: 157 alive / 155 gold
- SOCKS5: 162 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43617
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
