# SyndProxy private pool

## Current pool

- Alive now: 709
- Gold now: 375
- HTTP: 161 alive / 73 gold
- HTTPS: 134 alive / 18 gold
- SOCKS4: 205 alive / 138 gold
- SOCKS5: 209 alive / 146 gold

## Historical pool

- Discovered: 145568
- Ever alive: 25510
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
