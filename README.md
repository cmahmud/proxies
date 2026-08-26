# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 409
- HTTP: 102 alive / 66 gold
- HTTPS: 80 alive / 19 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38606
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
