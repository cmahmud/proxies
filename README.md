# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 428
- HTTP: 106 alive / 75 gold
- HTTPS: 41 alive / 20 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48984
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
