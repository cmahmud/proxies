# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 399
- HTTP: 87 alive / 58 gold
- HTTPS: 79 alive / 20 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38514
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
