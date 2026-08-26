# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 405
- HTTP: 104 alive / 62 gold
- HTTPS: 63 alive / 15 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38403
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
