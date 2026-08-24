# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 409
- HTTP: 111 alive / 71 gold
- HTTPS: 64 alive / 18 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33723
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
