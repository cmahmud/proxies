# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 428
- HTTP: 101 alive / 68 gold
- HTTPS: 50 alive / 20 gold
- SOCKS4: 190 alive / 167 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48904
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
