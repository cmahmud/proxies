# SyndProxy private pool

## Current pool

- Alive now: 687
- Gold now: 385
- HTTP: 185 alive / 72 gold
- HTTPS: 103 alive / 18 gold
- SOCKS4: 192 alive / 149 gold
- SOCKS5: 207 alive / 146 gold

## Historical pool

- Discovered: 147187
- Ever alive: 25844
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
