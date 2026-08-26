# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 399
- HTTP: 108 alive / 57 gold
- HTTPS: 83 alive / 12 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 197 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38256
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
