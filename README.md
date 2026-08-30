# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 445
- HTTP: 102 alive / 81 gold
- HTTPS: 43 alive / 30 gold
- SOCKS4: 165 alive / 163 gold
- SOCKS5: 176 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43684
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
