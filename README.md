# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 424
- HTTP: 102 alive / 72 gold
- HTTPS: 45 alive / 23 gold
- SOCKS4: 176 alive / 165 gold
- SOCKS5: 175 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49017
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
