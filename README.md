# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 446
- HTTP: 98 alive / 77 gold
- HTTPS: 106 alive / 31 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 191 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47354
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
