# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 424
- HTTP: 87 alive / 67 gold
- HTTPS: 55 alive / 27 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47069
- Ever gold: 1464

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
