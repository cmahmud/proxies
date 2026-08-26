# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 399
- HTTP: 98 alive / 58 gold
- HTTPS: 70 alive / 16 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38558
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
