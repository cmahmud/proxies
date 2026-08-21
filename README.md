# SyndProxy private pool

## Current pool

- Alive now: 944
- Gold now: 372
- HTTP: 308 alive / 83 gold
- HTTPS: 244 alive / 20 gold
- SOCKS4: 171 alive / 118 gold
- SOCKS5: 221 alive / 151 gold

## Historical pool

- Discovered: 158225
- Ever alive: 29875
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
