# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 405
- HTTP: 102 alive / 61 gold
- HTTPS: 67 alive / 15 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38401
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
