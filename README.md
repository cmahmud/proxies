# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 455
- HTTP: 126 alive / 84 gold
- HTTPS: 133 alive / 31 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 192 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46751
- Ever gold: 1449

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
