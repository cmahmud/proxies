# SyndProxy validated proxy pool

## Current pool

- Alive now: 665
- Gold now: 355
- HTTP: 128 alive / 79 gold
- HTTPS: 83 alive / 30 gold
- SOCKS4: 203 alive / 67 gold
- SOCKS5: 251 alive / 179 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48577
- Ever gold: 1546

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
