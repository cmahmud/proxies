# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 406
- HTTP: 108 alive / 62 gold
- HTTPS: 63 alive / 21 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38735
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
