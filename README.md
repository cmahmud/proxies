# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 414
- HTTP: 98 alive / 66 gold
- HTTPS: 178 alive / 20 gold
- SOCKS4: 183 alive / 159 gold
- SOCKS5: 196 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40702
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
