# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 423
- HTTP: 97 alive / 69 gold
- HTTPS: 45 alive / 22 gold
- SOCKS4: 194 alive / 162 gold
- SOCKS5: 179 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48879
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
