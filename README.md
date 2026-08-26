# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 405
- HTTP: 99 alive / 63 gold
- HTTPS: 67 alive / 18 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 193 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38681
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
