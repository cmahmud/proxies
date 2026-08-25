# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 400
- HTTP: 96 alive / 64 gold
- HTTPS: 86 alive / 21 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 177 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37572
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
