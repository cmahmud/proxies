# SyndProxy validated proxy pool

## Current pool

- Alive now: 733
- Gold now: 473
- HTTP: 195 alive / 98 gold
- HTTPS: 127 alive / 37 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 236 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45295
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
