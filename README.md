# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 414
- HTTP: 108 alive / 68 gold
- HTTPS: 73 alive / 21 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 172 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37761
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
