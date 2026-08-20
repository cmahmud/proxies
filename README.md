# SyndProxy private pool

## Current pool

- Alive now: 686
- Gold now: 386
- HTTP: 186 alive / 73 gold
- HTTPS: 103 alive / 18 gold
- SOCKS4: 190 alive / 149 gold
- SOCKS5: 207 alive / 146 gold

## Historical pool

- Discovered: 147187
- Ever alive: 25844
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
