# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 421
- HTTP: 96 alive / 67 gold
- HTTPS: 44 alive / 21 gold
- SOCKS4: 192 alive / 163 gold
- SOCKS5: 201 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48920
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
