# SyndProxy private pool

## Current pool

- Alive now: 948
- Gold now: 375
- HTTP: 304 alive / 84 gold
- HTTPS: 240 alive / 21 gold
- SOCKS4: 173 alive / 119 gold
- SOCKS5: 231 alive / 151 gold

## Historical pool

- Discovered: 158225
- Ever alive: 29873
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
