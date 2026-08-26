# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 411
- HTTP: 101 alive / 63 gold
- HTTPS: 77 alive / 14 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 209 alive / 172 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38174
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
