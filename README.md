# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 405
- HTTP: 98 alive / 63 gold
- HTTPS: 74 alive / 15 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 193 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39177
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
