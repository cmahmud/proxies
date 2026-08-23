# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 308
- HTTP: 158 alive / 37 gold
- HTTPS: 55 alive / 11 gold
- SOCKS4: 192 alive / 153 gold
- SOCKS5: 180 alive / 107 gold

## Historical pool

- Discovered: 171039
- Ever alive: 32828
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
