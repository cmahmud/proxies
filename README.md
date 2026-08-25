# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 390
- HTTP: 96 alive / 61 gold
- HTTPS: 80 alive / 17 gold
- SOCKS4: 164 alive / 157 gold
- SOCKS5: 167 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37366
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
