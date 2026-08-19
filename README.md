# SyndProxy private pool

## Current pool

- Alive now: 1320
- Gold now: 514
- HTTP: 512 alive / 181 gold
- HTTPS: 349 alive / 48 gold
- SOCKS4: 209 alive / 125 gold
- SOCKS5: 250 alive / 160 gold

## Historical pool

- Discovered: 125667
- Ever alive: 19647
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
