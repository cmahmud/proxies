# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 452
- HTTP: 125 alive / 83 gold
- HTTPS: 100 alive / 38 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46978
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
