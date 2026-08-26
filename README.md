# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 389
- HTTP: 125 alive / 70 gold
- HTTPS: 171 alive / 20 gold
- SOCKS4: 163 alive / 147 gold
- SOCKS5: 177 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39757
- Ever gold: 1303

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
