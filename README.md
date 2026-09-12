# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 423
- HTTP: 105 alive / 76 gold
- HTTPS: 48 alive / 24 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49485
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
