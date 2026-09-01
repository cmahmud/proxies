# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 451
- HTTP: 125 alive / 81 gold
- HTTPS: 131 alive / 33 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 197 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46746
- Ever gold: 1449

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
