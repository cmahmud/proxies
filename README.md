# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 424
- HTTP: 94 alive / 68 gold
- HTTPS: 60 alive / 27 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47069
- Ever gold: 1464

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
