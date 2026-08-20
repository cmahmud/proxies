# SyndProxy private pool

## Current pool

- Alive now: 737
- Gold now: 402
- HTTP: 171 alive / 80 gold
- HTTPS: 145 alive / 20 gold
- SOCKS4: 198 alive / 151 gold
- SOCKS5: 223 alive / 151 gold

## Historical pool

- Discovered: 151073
- Ever alive: 27502
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
