# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 411
- HTTP: 99 alive / 63 gold
- HTTPS: 81 alive / 18 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39100
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
