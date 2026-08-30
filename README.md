# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 446
- HTTP: 127 alive / 91 gold
- HTTPS: 72 alive / 34 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 204 alive / 163 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44252
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
