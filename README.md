# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 389
- HTTP: 74 alive / 50 gold
- HTTPS: 55 alive / 15 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 178 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41635
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
