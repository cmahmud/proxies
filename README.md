# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 391
- HTTP: 72 alive / 50 gold
- HTTPS: 58 alive / 16 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 177 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41635
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
