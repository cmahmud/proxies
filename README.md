# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 371
- HTTP: 80 alive / 51 gold
- HTTPS: 40 alive / 12 gold
- SOCKS4: 163 alive / 152 gold
- SOCKS5: 181 alive / 156 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33041
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
