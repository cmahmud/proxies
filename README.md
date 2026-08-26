# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 406
- HTTP: 85 alive / 62 gold
- HTTPS: 65 alive / 18 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 191 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38533
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
