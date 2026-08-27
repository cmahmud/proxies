# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 418
- HTTP: 94 alive / 73 gold
- HTTPS: 116 alive / 18 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 192 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41405
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
