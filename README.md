# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 406
- HTTP: 88 alive / 62 gold
- HTTPS: 71 alive / 19 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38533
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
