# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 461
- HTTP: 152 alive / 91 gold
- HTTPS: 125 alive / 35 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 196 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46872
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
