# SyndProxy private pool

## Current pool

- Alive now: 688
- Gold now: 385
- HTTP: 177 alive / 70 gold
- HTTPS: 110 alive / 20 gold
- SOCKS4: 191 alive / 149 gold
- SOCKS5: 210 alive / 146 gold

## Historical pool

- Discovered: 147187
- Ever alive: 25848
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
