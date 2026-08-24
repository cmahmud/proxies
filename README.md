# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 427
- HTTP: 134 alive / 77 gold
- HTTPS: 72 alive / 22 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33897
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
