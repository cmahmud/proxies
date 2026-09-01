# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 446
- HTTP: 101 alive / 77 gold
- HTTPS: 104 alive / 30 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 189 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47366
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
