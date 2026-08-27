# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 408
- HTTP: 102 alive / 59 gold
- HTTPS: 53 alive / 21 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41688
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
