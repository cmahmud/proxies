# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 421
- HTTP: 99 alive / 73 gold
- HTTPS: 46 alive / 20 gold
- SOCKS4: 176 alive / 165 gold
- SOCKS5: 178 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49002
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
