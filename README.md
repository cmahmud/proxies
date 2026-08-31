# SyndProxy validated proxy pool

## Current pool

- Alive now: 662
- Gold now: 463
- HTTP: 127 alive / 92 gold
- HTTPS: 131 alive / 33 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 227 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45762
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
