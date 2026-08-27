# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 392
- HTTP: 80 alive / 49 gold
- HTTPS: 53 alive / 15 gold
- SOCKS4: 178 alive / 164 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41669
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
