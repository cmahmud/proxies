# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 408
- HTTP: 95 alive / 63 gold
- HTTPS: 59 alive / 20 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41717
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
