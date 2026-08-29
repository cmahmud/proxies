# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 384
- HTTP: 95 alive / 63 gold
- HTTPS: 75 alive / 9 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 172 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43445
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
