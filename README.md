# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 402
- HTTP: 122 alive / 70 gold
- HTTPS: 62 alive / 17 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 184 alive / 161 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38941
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
