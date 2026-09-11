# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 428
- HTTP: 95 alive / 72 gold
- HTTPS: 61 alive / 26 gold
- SOCKS4: 177 alive / 167 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49053
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
