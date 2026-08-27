# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 393
- HTTP: 93 alive / 54 gold
- HTTPS: 41 alive / 14 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41658
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
