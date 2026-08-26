# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 401
- HTTP: 107 alive / 59 gold
- HTTPS: 79 alive / 16 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39026
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
