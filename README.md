# SyndProxy private pool

## Current pool

- Alive now: 648
- Gold now: 382
- HTTP: 161 alive / 67 gold
- HTTPS: 93 alive / 16 gold
- SOCKS4: 192 alive / 145 gold
- SOCKS5: 202 alive / 154 gold

## Historical pool

- Discovered: 146602
- Ever alive: 25690
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
