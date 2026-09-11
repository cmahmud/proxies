# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 417
- HTTP: 102 alive / 66 gold
- HTTPS: 42 alive / 20 gold
- SOCKS4: 188 alive / 162 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48875
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
