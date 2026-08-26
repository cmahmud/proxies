# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 399
- HTTP: 107 alive / 59 gold
- HTTPS: 90 alive / 12 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38261
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
