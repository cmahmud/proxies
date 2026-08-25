# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 417
- HTTP: 91 alive / 59 gold
- HTTPS: 73 alive / 22 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36205
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
