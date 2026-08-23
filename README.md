# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 364
- HTTP: 76 alive / 41 gold
- HTTPS: 34 alive / 9 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 184 alive / 159 gold

## Historical pool

- Discovered: 173056
- Ever alive: 33002
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
