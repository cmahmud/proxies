# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 342
- HTTP: 126 alive / 38 gold
- HTTPS: 70 alive / 10 gold
- SOCKS4: 171 alive / 152 gold
- SOCKS5: 180 alive / 142 gold

## Historical pool

- Discovered: 171039
- Ever alive: 32824
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
