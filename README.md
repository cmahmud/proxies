# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 364
- HTTP: 73 alive / 41 gold
- HTTPS: 39 alive / 9 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 187 alive / 159 gold

## Historical pool

- Discovered: 173056
- Ever alive: 33001
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
