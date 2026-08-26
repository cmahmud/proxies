# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 403
- HTTP: 93 alive / 60 gold
- HTTPS: 91 alive / 15 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39166
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
