# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 441
- HTTP: 105 alive / 81 gold
- HTTPS: 45 alive / 27 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 176 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43686
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
