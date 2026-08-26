# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 411
- HTTP: 107 alive / 67 gold
- HTTPS: 95 alive / 14 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38130
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
