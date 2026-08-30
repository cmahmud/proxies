# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 445
- HTTP: 98 alive / 84 gold
- HTTPS: 45 alive / 28 gold
- SOCKS4: 166 alive / 162 gold
- SOCKS5: 178 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43684
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
