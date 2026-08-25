# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 414
- HTTP: 108 alive / 73 gold
- HTTPS: 92 alive / 13 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34873
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
