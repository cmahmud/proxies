# SyndProxy private pool

## Current pool

- Alive now: 771
- Gold now: 390
- HTTP: 184 alive / 75 gold
- HTTPS: 152 alive / 19 gold
- SOCKS4: 229 alive / 150 gold
- SOCKS5: 206 alive / 146 gold

## Historical pool

- Discovered: 150516
- Ever alive: 27042
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
