# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 350
- HTTP: 115 alive / 43 gold
- HTTPS: 79 alive / 12 gold
- SOCKS4: 158 alive / 153 gold
- SOCKS5: 180 alive / 142 gold

## Historical pool

- Discovered: 171032
- Ever alive: 32808
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
