# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 411
- HTTP: 104 alive / 66 gold
- HTTPS: 109 alive / 17 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41407
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
