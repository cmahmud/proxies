# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 406
- HTTP: 108 alive / 68 gold
- HTTPS: 66 alive / 19 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 166 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37303
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
