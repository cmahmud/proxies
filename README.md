# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 463
- HTTP: 146 alive / 92 gold
- HTTPS: 114 alive / 36 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46878
- Ever gold: 1455

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
