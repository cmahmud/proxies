# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 408
- HTTP: 111 alive / 64 gold
- HTTPS: 82 alive / 15 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37998
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
