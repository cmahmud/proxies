# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 400
- HTTP: 97 alive / 62 gold
- HTTPS: 89 alive / 21 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 181 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37583
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
