# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 370
- HTTP: 80 alive / 45 gold
- HTTPS: 34 alive / 10 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 184 alive / 159 gold

## Historical pool

- Discovered: 173056
- Ever alive: 33006
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
