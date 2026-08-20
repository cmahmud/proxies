# SyndProxy private pool

## Current pool

- Alive now: 674
- Gold now: 377
- HTTP: 174 alive / 70 gold
- HTTPS: 107 alive / 21 gold
- SOCKS4: 191 alive / 140 gold
- SOCKS5: 202 alive / 146 gold

## Historical pool

- Discovered: 147187
- Ever alive: 25820
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
