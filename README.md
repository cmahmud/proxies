# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 392
- HTTP: 97 alive / 66 gold
- HTTPS: 38 alive / 21 gold
- SOCKS4: 169 alive / 131 gold
- SOCKS5: 191 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48761
- Ever gold: 1565

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
