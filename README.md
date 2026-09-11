# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 424
- HTTP: 91 alive / 70 gold
- HTTPS: 60 alive / 26 gold
- SOCKS4: 197 alive / 167 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49074
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
