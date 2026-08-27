# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 399
- HTTP: 90 alive / 54 gold
- HTTPS: 55 alive / 20 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41696
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
