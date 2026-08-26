# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 424
- HTTP: 89 alive / 69 gold
- HTTPS: 78 alive / 22 gold
- SOCKS4: 171 alive / 164 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37970
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
