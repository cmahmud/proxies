# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 409
- HTTP: 96 alive / 64 gold
- HTTPS: 91 alive / 19 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38057
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
