# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 419
- HTTP: 103 alive / 73 gold
- HTTPS: 44 alive / 19 gold
- SOCKS4: 181 alive / 165 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49012
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
