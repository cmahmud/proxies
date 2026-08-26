# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 407
- HTTP: 106 alive / 64 gold
- HTTPS: 87 alive / 14 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38001
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
