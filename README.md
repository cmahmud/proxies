# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 399
- HTTP: 108 alive / 62 gold
- HTTPS: 59 alive / 13 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38355
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
